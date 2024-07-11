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
        'date': datetime.datetime(2006, 3, 21, 12, 50)
    }

@pytest.fixture
def jun_2012_memento_20():
    url = "http://web.archive.org/web/20120608132840/https://twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def test_jun_2012_20(tweet_id_20, jun_2012_memento_20):
    extracted_contents = getters2012.get_jun_2012(jun_2012_memento_20)
    assert extracted_contents == tweet_id_20
