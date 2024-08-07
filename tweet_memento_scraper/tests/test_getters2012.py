from getters import getters2008_2011, getters2012
import datetime
import pytest
import requests
from bs4 import BeautifulSoup

# Fixtures representing what we expect from our test Tweet IDs
@pytest.fixture
def tweet_id_20():
    return {
        'tweet-text': "just setting up my twttr",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2006, 3, 21)
    }

@pytest.fixture
def tweet_id_160052090721419264():
    return {
        'tweet-text': "A photo of David Hasselhoff is in my Discover tab. #germany",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2012, 1, 19)
    }

@pytest.fixture
def jan_2012_memento_160052090721419264():
    url = "http://web.archive.org/web/20120120050548/https://twitter.com//jack/status/160052090721419264"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jan_2012_memento_20():
    url = "http://web.archive.org/web/20120112171012/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def march_2012_memento_20():
    url = "http://web.archive.org/web/20120322170404/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jun_2012_memento_20():
    url = "http://web.archive.org/web/20120608132840/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def nov_2012_memento_20():
    url = "http://web.archive.org/web/20121124085527/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def dec_2012_memento_20():
    url = "http://web.archive.org/web/20121223123054/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')



def test_jan_2012_160052090721419264(tweet_id_160052090721419264, jan_2012_memento_160052090721419264):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(jan_2012_memento_160052090721419264)
    assert extracted_contents == tweet_id_160052090721419264


def test_jan_2012_20(tweet_id_20, jan_2012_memento_20):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(jan_2012_memento_20)
    assert extracted_contents == tweet_id_20

def test_march_2012_20(tweet_id_20, march_2012_memento_20):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(march_2012_memento_20)
    assert extracted_contents == tweet_id_20


def test_jun_2012_20(tweet_id_20, jun_2012_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(jun_2012_memento_20)
    assert extracted_contents == tweet_id_20

def test_nov_2012_20(tweet_id_20, nov_2012_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(nov_2012_memento_20)
    assert extracted_contents == tweet_id_20

def test_dec_2012_20(tweet_id_20, dec_2012_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(dec_2012_memento_20)
    assert extracted_contents == tweet_id_20
