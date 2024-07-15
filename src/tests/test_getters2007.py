# from getters import getters2008_2011, getters2012
import datetime
import pytest
import requests
from bs4 import BeautifulSoup
from getters import getters2007

@pytest.fixture
def tweet_id_5254943():
    return {
        'tweet-text': "NyQuil sleep is not good sleep, but sleep nonetheless.",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2007, 2, 3)
    }

@pytest.fixture
def feb_2007_memento_5254943():
    url = "http://web.archive.org/web/20070218034409/twitter.com/jack/statuses/5254943"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def test_feb_2007_5254943(tweet_id_5254943, feb_2007_memento_5254943):
    extracted_contents = getters2007.get_feb_2012(feb_2007_memento_5254943)
    assert extracted_contents == tweet_id_5254943