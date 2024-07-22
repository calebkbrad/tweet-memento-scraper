from datetime import datetime
from bs4 import BeautifulSoup

def get_memento_datetime(response_headers: dict) -> datetime:
    """
    Extract appropriate datetime from Memento datetime header

    Parameters
    ----------
    response_headers: The response headers from a request to the Wayback Machine

    Returns
    ----------
    datetime object corresponding to the "memento-datetime" header in the response_headers
    """

    memento_datetime_header = response_headers['memento-datetime']
    return datetime.strptime(memento_datetime_header, "%a, %d %b %Y %H:%M:%S GMT")

