from datetime import datetime
from enum import IntEnum
from requests import Response
import requests
from bs4 import BeautifulSoup
from ..getters import getters2007, getters2008_2011, getters2012, getters2022

class Timeframe(IntEnum):
    UNKNOWN_BEFORE = 0
    FEB_2007_TO_AUG_2008 = 1
    SEP_2008_TO_NOV_2008 = 2
    DEC_2008_TO_APRIL_2012 = 3
    MAY_2012_TO_MAY_2022 = 4
    JUN_2022 = 5

getters_list = [
    None,
    getters2007.get_feb_2007_to_aug_2008,
    getters2008_2011.get_sep_2008_to_nov_2008,
    getters2008_2011.get_dec_2008_to_april_2012,
    getters2012.get_may_2012_to_may_2022,
    getters2022.get_jun_2022
]

def get_memento_datetime(response: Response) -> datetime:
    """
    Extract appropriate datetime from Memento datetime header

    Parameters
    ----------
    response_headers: The HTTP response from a request to a Wayback Machine memento

    Returns
    ----------
    datetime object corresponding to the "memento-datetime" header in the response_headers
    """

    memento_datetime_header = response.headers['memento-datetime']
    return datetime.strptime(memento_datetime_header, "%a, %d %b %Y %H:%M:%S GMT")

def get_tweet_memento_timeframe(memento_datetime: datetime) -> Timeframe:
    """
    Determines the timeframe in which a memento occurred given the datetime equivalent of its memento-datetime header. 

    Parameters
    ----------
    memento_datetime: The datetime value extracted from the memento's memento-datetime header
    Returns
    ----------
    The timeframe that this memento occurred in as a Timeframe enum
    """
    timeframes = (
        (datetime(2007, 2, 1), datetime(2008, 8, 31), Timeframe.FEB_2007_TO_AUG_2008),
        (datetime(2008, 9, 1), datetime(2008, 11, 30), Timeframe.SEP_2008_TO_NOV_2008),
        (datetime(2008, 12, 1), datetime(2012, 4, 30), Timeframe.DEC_2008_TO_APRIL_2012),
        (datetime(2012, 5, 1), datetime(2022, 5, 31), Timeframe.MAY_2012_TO_MAY_2022),
    )

    # Handle tweets older than known and last range
    if memento_datetime < datetime(2007, 2, 1):
        return Timeframe.UNKNOWN_BEFORE
    if memento_datetime > datetime(2022, 5, 31):
        return Timeframe.JUN_2022
    
    # Handle all intermediate ranges
    for timeframe in timeframes:
        if timeframe[0] <= memento_datetime <= timeframe[1]:
            return timeframe[2]
    
    # Memento cannot be placed
    raise ValueError("f{memento_datetime} could not be placed in any timeframe")



def scrape_tweet(uri: str) -> dict:
    """
    Scrape the tweet for available info, return as dict
    """
    response = requests.get(uri)
    soup = BeautifulSoup(response.content, 'html.parser')
    memento_datetime = get_memento_datetime(response)
    timeframe = get_tweet_memento_timeframe(memento_datetime)

    return getters_list[int(timeframe)](soup)
