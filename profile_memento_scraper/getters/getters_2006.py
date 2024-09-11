from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_2006(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa 2006.

    Parameters
    ------------
    content: A BeautifulSoup object with the content of a profile page from this timeframe
    
    Returns
    ------------
    dict
        Dictionary containing all available information, including the following:
        handle: The current username of the user
        full-name: The current screen name of the user
        archived-at: The memento-datetime of the menento as a datetime
    """
    
