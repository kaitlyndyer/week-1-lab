

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
        """This method checks to see if the single observation has valid usable data"""
        return self.avg_speed is not None and self.total_volume is not None
    
    def __lt__(self, other):
        """This compares observations based on their time to sort"""
        return self.time < other.time
    
    def __str__(self):
        """This returns a readable string representation of the data for the user"""
        return (f'Site: {self.site_name}, Date: {self.date}, Time: {self.time}, Speed: {self.avg_speed}, Volume: {self.total_volume}')
    
    class Site:
        def __init__(self, site_id, site_name, observations):
            self.site_id = site_id
            self.site_name = site_name
            self.observations = observations




    