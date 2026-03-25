from webtris_client import Site, WebTRISClient

def main():
    """I used the same formate as the labs, creating a main function to show how the traffic analysis works"""

    # first we create a client
    client = WebTRISClient("https://webtris.nationalhighways.co.uk/api/v1.0")

    # Then we get the observations for a single given day
    observations = client.get_daily_observations(461, "19102025")

    # In case if there is no usable data
    if not observations:
        return print("There is no data")

    # Now we create the Site object
    site_name = observations[0].site_name
    site = Site(461, site_name, observations)

    # Now that we have setup the observations and the site we can test the results
    print("General Site Analysis-----")
    print(f"Average Speed: {site.get_average_speed()}")
    print(f"Total Volume: {site.get_total_volume()}")
    
    print("Hour Analysis-------------")
    print(f"Average Speed at 00: {site.get_average_speed_for_given_hour('00')}")
    print(f"Total Volume at 00: {site.get_total_volume_for_given_hour('00')}")
    print(f"Average Speed at 01: {site.get_average_speed_for_given_hour('01')}")
    print(f"Total Volume at 01: {site.get_total_volume_for_given_hour('01')}")
    
    print("Peak Hour-----------------")
    print(f"Peak Hour: {site.get_peak_hour()}")

if __name__ == "__main__":
    main()





