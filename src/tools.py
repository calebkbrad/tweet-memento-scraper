from datetime import datetime
from enum import Enum

class Timeframe(Enum):
    FEB_2007_TO_AUG_2008 = 1
    SEP_2008_TO_NOV_2008 = 2
    DEC_2008_TO_APRIL_2012 = 3
    MAY_2012_TO_MAY_2022 = 4
    JUN_2022 = 5

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


