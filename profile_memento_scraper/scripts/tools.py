from datetime import datetime
from enum import IntEnum
from requests import Response, Session
from bs4 import BeautifulSoup
from time import sleep
from googletrans import Translator
import requests
from ..getters import getters_2006, getters_2007, getters_2008, getters_2009_2010, getters_2011, getters_2012_2013, getters_2014, getters_2015_2021, getters_2022

class Timeframe(IntEnum):
    UNKNOWN_BEFORE = 0
    NOV_2006_TO_JUL_2007 = 1
    AUG_2007_TO_SEP_2008 = 2
    OCT_2008_TO_FEB_2009 = 3
    MAR_2009_TO_NOV_2011 = 4
    DEC_2011_TO_APR_2012 = 5
    MAY_2012_TO_APR_2014 = 6
    JUN_2014_TO_JUL_2014 = 7
    JUL_2014_TO_MAY_2015 = 8
    MAY_2015_TO_JUN_2022 = 9
    JUL_2022 = 10
    AFTER_NOV_2023 = 11

getters_list = [
    None,
    getters_2006.get_profile_nov_2006_jul_2007,
    getters_2007.get_profile_aug_2007,
    getters_2008.get_profile_oct_2008,
    getters_2009_2010.get_profile_mar_2009,
    getters_2011.get_profile_dec_2011,
    getters_2012_2013.get_profile_may_2012,
    getters_2014.get_profile_may_2014,
    getters_2014.get_profile_jul_2014,
    getters_2015_2021.get_profile_may_2015,
    getters_2022.get_profile_jun_2022
]

timeframes = (
    (datetime(2006, 11, 1), datetime(2008, 7, 31), Timeframe.NOV_2006_TO_JUL_2007),
    (datetime(2007, 8, 1), datetime(2008, 9, 30), Timeframe.AUG_2007_TO_SEP_2008),
    (datetime(2008, 10, 1), datetime(2009, 2, 28), Timeframe.OCT_2008_TO_FEB_2009),
    (datetime(2009, 3, 1), datetime(2011, 11, 30), Timeframe.MAR_2009_TO_NOV_2011),
    (datetime(2011, 12, 1), datetime(2012, 4, 30), Timeframe.DEC_2011_TO_APR_2012),
    (datetime(2012, 5, 1), datetime(2014, 4, 30), Timeframe.MAY_2012_TO_APR_2014),
    (datetime(2014, 5, 1), datetime(2014, 6, 30), Timeframe.JUN_2014_TO_JUL_2014),
    (datetime(2014, 7, 1), datetime(2015, 5, 29), Timeframe.JUL_2014_TO_MAY_2015),
    (datetime(2015, 5, 30), datetime(2022, 6, 25), Timeframe.MAY_2015_TO_JUN_2022)
)

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

def get_profile_memento_timeframe(memento_datetime: datetime) -> Timeframe:
    """
    Determines the timeframe in which a memento occurred given the datetime equivalent of its memento-datetime header. 

    Parameters
    ----------
    memento_datetime: The datetime value extracted from the memento's memento-datetime header
    Returns
    ----------
    The timeframe that this memento occurred in as a Timeframe enum
    """

    # Handle timeframe older than Nov 2023 (scraping will be unsuccessful)
    if memento_datetime > datetime(2023, 11, 1):
        return Timeframe.AFTER_NOV_2023
    # Handle tweets older than known and last range
    if memento_datetime < datetime(2006, 11, 1):
        return Timeframe.UNKNOWN_BEFORE
    if memento_datetime > datetime(2022, 6, 26):
        return Timeframe.JUL_2022
    
    # Handle all intermediate ranges
    for timeframe in timeframes:
        if timeframe[0] <= memento_datetime <= timeframe[1]:
            return timeframe[2]
    
    # Memento cannot be placed
    raise ValueError(f"{memento_datetime} could not be placed in any timeframe")

def scrape_single_profile(uri: str):
    """
    Scrape the tweet for available info, return as dict. This will be called specifically by the command to scrape a single tweet

    Parameters
    ----------
    uri: A URI-R of a Twitter profile page

    Returns
    ----------
    The dictionary representing a tweet with the following fields where possible, labelled by URI:
    full-name: Full name of the profile archived
    handle: The handle of the profile archived
    tweets: List of all the available tweets from the archived page. Each item contains the text of the tweet and the date it was made in iso format
    archived-at: datetime of the date the memento was archived in iso format
    """
    print(f"Getting {uri}")
    response = requests.get(uri)
    print("Request successful")
    soup = BeautifulSoup(response.content, 'html.parser')
    memento_datetime = get_memento_datetime(response)
    timeframe = get_profile_memento_timeframe(memento_datetime)
    if timeframe == Timeframe.AFTER_NOV_2023:
        raise ValueError("URI is archived after November 2023, scraping is not possible")
    info = getters_list[int(timeframe)](soup)
    info['archived-at'] = memento_datetime.isoformat()
    convert_tweet_dates(info['tweets'])
    # if type(info['date']) == datetime:
    #     info['date'] = info['date'].isoformat()
    return info

def scrape_profile(uri: str, session: Session, fast: bool, wait_time: float = 5) -> dict:
    """
    Scrape the tweet for available info, return as dict
    This function also adds the memento's datetime header as the field 'archived-at'

    Parameters
    ----------
    uri: A URI-R of a Twitter status URI from the Wayback Machine
    session: A requests http session
    fast: Whether or not to wait between requests to ease load on Wayback Machine and prevent connection refusals
    wait_time: Number of seconds to wait between requests when fast mode is disabled

    Returns
    ----------
    The dictionary representing a tweet with the following fields where possible, labelled by URI:
    tweet-text: The tweet body
    full-name: Full name of the tweet author
    handle: Twitter handle of the tweet author
    date: datetime of the date the tweet was made in iso. This field truncates precision from hour onwards
    archived-at: datetime of the date the memento was archived in iso
    """
    print(f"Getting {uri}")
    response = session.get(uri)
    print("Request successful")
    if not fast:
        print("Waiting")
        sleep(wait_time)
            
    soup = BeautifulSoup(response.content, 'html.parser')
    memento_datetime = get_memento_datetime(response)
    timeframe = get_profile_memento_timeframe(memento_datetime)
    if timeframe == Timeframe.AFTER_NOV_2023:
        raise ValueError("URI is archived after November 2023, scraping is not possible")
    info = getters_list[int(timeframe)](soup)
    info['archived-at'] = memento_datetime.isoformat()
    convert_tweet_dates(info['tweets'])
    # if type(info['date']) == datetime:
    #     info['date'] = info['date'].isoformat()
    return info

def validate_date(date_string: str) -> datetime | None:
    """
    Attempt to validate the timestamp extracted from the page and return it as a datetime
    Can only try against time formats that I know about, so if none match, then None will be returned
    """
    translator = Translator()
    attempt_string = date_string.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")

    if 'en' not in translator.detect(attempt_string).lang:
        attempt_string = translator.translate(attempt_string).text.strip()
    formats = [
        "%I:%M %p - %d %b %y",
        "%I:%M %p - %d %b %Y",
        "%I:%M - %d %b %Y",
        "%I:%M %p - %d %b %y (%Z%z)",
        "%I:%M - %B %d, %Y",
        "%I:%M - %d %b %Y",
        "%I:%M %p %b %d, %Y"
    ]
    date = None
    for format in formats:
        try:
            date = datetime.strptime(attempt_string, format)
            break
        except ValueError as er:
            # print(er)
            continue
    return date

def convert_tweet_dates(tweets: list):
    """
    
    """
    for tweet in tweets:
        converted_date = validate_date(tweet['date'])
        if(type(converted_date)) == datetime:
            tweet['date'] = converted_date.isoformat()