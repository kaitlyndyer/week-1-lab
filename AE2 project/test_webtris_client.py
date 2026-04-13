# test_webtris_client.py
import pytest
from unittest.mock import patch, Mock
from requests.exceptions import Timeout
from webtris_client import WebTRISClient, Site, TrafficObservation


@pytest.fixture
def mock_success_response():
    # Here we create a fake response
    response = Mock(status_cose=200)
    response.json.return_value = {
        "Rows": [
            {
                "Site": "M25/4432A",
                "Report Date": "2025-10-19T00:00:00",
                "Time Period Ending": "00:14:00",
                "Avg mph": "60",
                "Total Volume": "182"
            },
            {
                "Site": "M25/4432A",
                "Report Date": "2025-10-19T00:00:00",
                "Time Period Ending": "00:29:00",
                "Avg mph": "", # to simulate a missing data case
                "Total Volume": "150"
            }
        ]
    }
    return response

# Testing the clients
@patch('webtris_client.requests.get') # The patch decorator temporarily replace the request.get with the mock inside the test
def test_get_daily_observations(mock_get, mock_success_response) -> None:
    """This tests that the client parses the JSON into objects correctly"""
    # make the patched request.get function return the mock_success_response
    mock_get.return_value = mock_success_response 
    client = WebTRISClient("https://webtris.nationalhighways.co.uk/api/v1.0")

    results = client.get_daily_observations(461, "19102025")

    # We now check that the result that is returned has the data from the mock
    assert len(results) == 2
    assert results[0].avg_speed == 60.0
    assert isinstance(results[0], TrafficObservation)

@patch('webtris_client.requests.get')
def test_get_daily_observations_http_error(mock_get) -> None:
    """We have to test that the API error returns an empty list when it gets an error"""
    mock_get.side_effect = Timeout("Connection timed out") # Here we make an execption
    client = WebTRISClient("https://webtris.nationalhighways.co.uk/api/v1.0") # now we use the WebTRISClient as we normally do

    results = client.get_daily_observations(461, "19102025")

    assert results == []
    

# Testing the analysis
def test_site_calculations() -> None:
    """Tests that the average speed and total volume methods in the Site class"""
    observation1 = TrafficObservation("Site A", "Date", "00:00:00", 60.0, 100)
    observation2 = TrafficObservation("Site A", "Date", "00:15:00", 40.0, 200)

    test_site = Site(461, "Site A", [observation1, observation2])

    assert test_site.get_average_speed() == 50 
    assert test_site.get_total_volume() == 300
    assert len(test_site) == 2

def test_observation_is_valid() -> None:
    """This tests that the is_valid method in the TrafficObservation Class can identify when there is missing data"""
    valid_observation = TrafficObservation("Site A", "Date", "00:00:00", 60.0, 100)
    invalid_observation = TrafficObservation("Site A", "Date", "00:15:00", None, 200)

    assert valid_observation.is_valid() is True
    assert invalid_observation.is_valid() is False

def test_sorting_observations() -> None:
    """This tests that the observations will be sorted by time"""
    later = TrafficObservation("Site A", "Date", "10:00:00", 60.0, 100)
    earlier = TrafficObservation("Site A", "Date", "09:15:00", 40.0, 200)

    assert earlier < later