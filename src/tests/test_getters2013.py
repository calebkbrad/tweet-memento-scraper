from getters import getters2012
import datetime
import pytest
import requests
from bs4 import BeautifulSoup

@pytest.fixture
def tweet_id_20():
    return {
        'tweet-text': "just setting up my twttr",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2006, 3, 21)
    }

@pytest.fixture
def feb_2013_memento_20_spanish():
    url = "http://web.archive.org/web/20130213163028/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def apr_2013_memento_20():
    url = "http://web.archive.org/web/20130401185751/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jun_2013_memento_20():
    url = "http://web.archive.org/web/20130606062732/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def aug_2013_memento_20():
    url = "http://web.archive.org/web/20130814003018/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def oct_2013_memento_20_spanish():
    url = "http://web.archive.org/web/20131002045749/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def dec_2013_memento_20():
    url = "http://web.archive.org/web/20131215023215/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')


def test_feb_2013_20_spanish(tweet_id_20, feb_2013_memento_20_spanish):
    extracted_contents = getters2012.get_jun_2012(feb_2013_memento_20_spanish)
    assert extracted_contents == tweet_id_20

def test_apr_2013_20(tweet_id_20, apr_2013_memento_20):
    extracted_contents = getters2012.get_jun_2012(apr_2013_memento_20)
    assert extracted_contents == tweet_id_20

def test_jun_2013_20(tweet_id_20, jun_2013_memento_20):
    extracted_contents = getters2012.get_jun_2012(jun_2013_memento_20)
    assert extracted_contents == tweet_id_20

def test_aug_2013_20(tweet_id_20, aug_2013_memento_20):
    extracted_contents = getters2012.get_jun_2012(aug_2013_memento_20)
    assert extracted_contents == tweet_id_20

def test_oct_2013_20_spanish(tweet_id_20, oct_2013_memento_20_spanish):
    extracted_contents = getters2012.get_jun_2012(oct_2013_memento_20_spanish)
    assert extracted_contents == tweet_id_20

def test_dec_2013_20(tweet_id_20, dec_2013_memento_20):
    extracted_contents = getters2012.get_jun_2012(dec_2013_memento_20)
    assert extracted_contents == tweet_id_20
