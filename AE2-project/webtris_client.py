import requests
from requests.exceptions import RequestException, Timeout, HTTPError


class Site:
    """This is a traffic site the monitors many observations"""
    def __init__(self, site_id: str, site_name: str, observations: list[TrafficObservation]):
        """Here we initialize the Site class with an ID, name and a list of observations"""
        self.site_id = site_id
        self.site_name = site_name
        self.observations = observations

    def __len__(self):
        return len(self.observations)
    
    def __iter__(self):
        for observation in sorted(self.observations):
            yield observation

    def get_average_speed(self):
        """This method calculates the average speed of all valid observations (using the method in the TrafficObservation class to check if it is valid)"""
        total_speed = 0
        count = 0

        # This iterates through each observation object in the list of observations
        for observer in self.observations:
            # Here we check that there is no missing values
            if observer.is_valid():
                # Here we accumulate the speeds
                total_speed += observer.avg_speed
                # And increase the total count of valid observations to find the average speed
                count += 1

        # we have to stop any divison by zero if there is no valid data 
        if count == 0:
            return None
        
        return total_speed / count
    
    def get_total_volume(self):
        """This method returns the total traffic volume for all of the valid observations"""
        total = 0

        # Here we do almost the same thing as the get_average_speed and iterate through the observations and accumulate the total
        for observer in self.observations:
            if observer.is_valid():
                total += observer.total_volume

        return total
    
    def get_average_speed_for_given_hour(self, hour):
        """This returns the average speed for a given specific hour"""
        total_speed = 0
        count = 0
        for observer in self.observations:
            # Here we get the hour using string slicing and filter through finding only the matching hour we are looking for
            if observer.is_valid() and observer.time[:2] == hour:
                total_speed += observer.avg_speed
                count += 1

        # Here we have to make sure that we are not dividing by zero
        if count == 0:
            return None
        
        return total_speed / count
    
    def get_total_volume_for_given_hour(self, hour):
        """This returns the total volume for a given hour"""
        total = 0

        # Here we follow the same idea and iterate through observations, filtering and checking the values
        for observer in self.observations:
            if observer.is_valid() and observer.time[:2] == hour:
                total += observer.total_volume

        return total
    

    def get_peak_hour(self):
        """This returns the hour that has the highest amount of traffic volume"""
        # Here we create a dictionary to hold the information with teh hour and then the total volume for each hour
        hour_volume_totals = {}

        # This loops through all the observers in the TrafficObervation
        for observer in self.observations:
            # This checks if there is valid data, ignoring any missing values
            if observer.is_valid():
                # Here we get the hour with slicing
                hour = observer.time[:2]

                # Here if the hours is not in the dictionary we add it
                if hour not in hour_volume_totals:
                    hour_volume_totals[hour] = 0

                hour_volume_totals[hour] += observer.total_volume

        # Here we avoid any errors by including this so that if there is no valid data we return None
        if not hour_volume_totals:
            return None
        
        # We find the hour with the highest toal volume by using max() to look through the dictionary and returns the key with the largest volume of traffic
        peak_hour = max(hour_volume_totals, key=hour_volume_totals.get)

        return peak_hour
        

class WebTRISClient:
    """This is a client class that manages all communitcation with the WebTRIS API"""
    def __init__(self, base_url: str):
        """This initalizes the class and the base_url is the URL of the WebTRIS API"""
        self.base_url = base_url

    def get_daily_observations(self, site_id: int, date: str):
        """This sends a GET request to an HTTP to get the traffic data for a single day"""
        try:
            # Making the HTTP GET request
            response = requests.get(
                f"{self.base_url}/reports/daily",
                params={
                    "sites": site_id, 
                    "start_date": date, 
                    "end_date": date,
                    "page": 1,
                    "page_size": 500}, # They are the same date to avoid pagination
                timeout=10) # Without this, the request could hang indefinitely
            
            # Converts 4xx/5xx status codes into exceptions so that we can catch them
            response.raise_for_status()

            # Coverting the JSON into a Python dictionary
            data = response.json()
        
        # Handling expections
        except Timeout:
            # Specific errors come first
            print("Request timed out - server may be busy")
            return []
        
        except HTTPError as e:
            # HTTPError is a broader class of error
            print(f"HTTP error occurred: {e.response.status_code}")
            return []
        
        except RequestException as e:
            # Catch all other RequestExceptions
            print(f"Network error: {e}")
            return []
        
        # Parse JSON into Python list
        observations = []

        rows = data.get("Rows", [])

        for row in rows:
            # we have to get the values from the JSON reponse
            avg_speed = row.get("Avg mph")
            total_volume = row.get("Total Volume")

            # We have to handle any missing data
            if avg_speed == "" or avg_speed is None:
                avg_speed = None
            else:
                avg_speed = float(avg_speed) # type casting

            if total_volume == "" or total_volume is None:
                total_volume = None
            else:
                total_volume = int(total_volume) # type casting

            # Now we create an object with all the parameters
            observation = TrafficObservation(
                site_name = row.get("Site Name"),
                date = row.get("Report Date"),
                time = row.get("Time Period Ending"),
                avg_speed = avg_speed,
                total_volume = total_volume
            )

            observations.append(observation)

            # Now we return the observations
        return observations 


class TrafficObservation:
    """This is an observer class that shows a single observation from a 15 minute interval"""
    def __init__(self, site_name, date, time, avg_speed, total_volume):
        """Here we are initializing the TrafficObservation object"""
        self.site_name = site_name
        self.date = date
        self.time = time
        self.avg_speed = avg_speed
        self.total_volume = total_volume

    def is_valid(self):
        """This method checks to see if the single observation has valid usable data (no missing values)"""
        return self.avg_speed is not None and self.total_volume is not None
    
    def __lt__(self, other):
        """This defines comparision to allow for us to sort by time"""
        return self.time < other.time
    
    def __str__(self):
        """This returns a readable string representation of the object for the user"""
        return (f'Site: {self.site_name}, Date: {self.date}, Time: {self.time}, Speed: {self.avg_speed}, Volume: {self.total_volume}')