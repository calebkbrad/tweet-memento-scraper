import datetime
import pytest
import requests
from bs4 import BeautifulSoup
from tools import get_memento_datetime, get_tweet_memento_timeframe
from tools import Timeframe

@pytest.fixture
def datetime_before_known():
    return datetime.datetime(2006, 1, 1)

@pytest.fixture
def datetime_last_range():
    return datetime.datetime(2023, 1, 1)

@pytest.fixture
def feb_2007_memento_5254943():
    url = "http://web.archive.org/web/20070218034409/twitter.com/jack/statuses/5254943"
    response = requests.get(url)
    return response

@pytest.fixture
def dec_22_2008_memento_20():
    url = "http://web.archive.org/web/20081222104434/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return response

@pytest.fixture
def jul_2010_memento_20():
    url = "http://web.archive.org/web/20100729145054/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return response

@pytest.fixture
def dec_2012_memento_20():
    url = "http://web.archive.org/web/20121223123054/twitter.com/jack/status/20"
    response = requests.get(url)
    return response

def test_get_before_timeframe(datetime_before_known):
    timeframe = get_tweet_memento_timeframe(datetime_before_known)
    assert timeframe == Timeframe.UNKNOWN_BEFORE

def test_get_feb_2007_timeframe(feb_2007_memento_5254943):
    memento_datetime = get_memento_datetime(feb_2007_memento_5254943)
    timeframe = get_tweet_memento_timeframe(memento_datetime)
    assert timeframe == Timeframe.FEB_2007_TO_AUG_2008

def test_get_dec_22_2008_timeframe(dec_22_2008_memento_20):
    memento_datetime = get_memento_datetime(dec_22_2008_memento_20)
    timeframe = get_tweet_memento_timeframe(memento_datetime)
    assert timeframe == Timeframe.DEC_2008_TO_APRIL_2012

def test_get_jul_2010_timeframe(jul_2010_memento_20):
    memento_datetime = get_memento_datetime(jul_2010_memento_20)
    timeframe = get_tweet_memento_timeframe(memento_datetime)
    assert timeframe == Timeframe.DEC_2008_TO_APRIL_2012

def test_get_dec_2012_timeframe(dec_2012_memento_20):
    memento_datetime = get_memento_datetime(dec_2012_memento_20)
    timeframe = get_tweet_memento_timeframe(memento_datetime)
    assert timeframe == Timeframe.MAY_2012_TO_MAY_2022

def test_get_last_timeframe(datetime_last_range):
    timeframe = get_tweet_memento_timeframe(datetime_last_range)
    assert timeframe == Timeframe.JUN_2022
