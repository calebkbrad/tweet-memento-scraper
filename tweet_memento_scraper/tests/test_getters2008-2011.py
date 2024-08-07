from getters import getters2008_2011
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
def tweet_id_968105771():
    return {
        'tweet-text': '"Don\'t make something unless it is both necessary and useful; but if it is both, don\'t hesitate to make it beautiful."',
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2008, 10, 20)
    }

# Fixtures to hold the requested HTML structure from the Wayback Machine
@pytest.fixture
def nov_2008_memento_20():
    url = "http://web.archive.org/web/20081103142857/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def sep_2009_memento_968105771():
    url = "http://web.archive.org/web/20090924111048/https://twitter.com/jack/status/968105771"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def dec_2008_memento_20():
    url = "http://web.archive.org/web/20081222104434/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def nov_2009_memento_20():
    url = "http://web.archive.org/web/20091101160459/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jul_2010_memento_20():
    url = "http://web.archive.org/web/20100729145054/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def apr_2011_memento_20():
    url = "http://web.archive.org/web/20110410174608/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def test_nov_2008_20(tweet_id_20, nov_2008_memento_20):
    extracted_contents = getters2008_2011.get_sep_2008_to_nov_2008(nov_2008_memento_20)
    assert extracted_contents == tweet_id_20

def test_dec_2008_20(tweet_id_20, dec_2008_memento_20):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(dec_2008_memento_20)
    assert extracted_contents == tweet_id_20

def test_sep_2009_968105771(tweet_id_968105771, sep_2009_memento_968105771):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(sep_2009_memento_968105771)
    assert extracted_contents == tweet_id_968105771

def test_nov_2009_20(tweet_id_20, nov_2009_memento_20):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(nov_2009_memento_20)
    assert extracted_contents == tweet_id_20

def test_jul_2010_20(tweet_id_20, jul_2010_memento_20):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(jul_2010_memento_20)
    assert extracted_contents == tweet_id_20

def test_apr_2011_20(tweet_id_20, apr_2011_memento_20):
    extracted_contents = getters2008_2011.get_dec_2008_to_april_2012(apr_2011_memento_20)
    assert extracted_contents == tweet_id_20
