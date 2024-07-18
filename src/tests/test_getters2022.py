from getters import getters2022
import datetime
import pytest
import requests
from bs4 import BeautifulSoup

@pytest.fixture
def tweet_id_20():
    return {
        'tweet-text': "just setting up my twttr",
        'full-name': "jack⚡️",
        'handle': "jack",
        'date': datetime.datetime(2006, 3, 21)
    }

@pytest.fixture
def jan_2022_memento_20():
    url = "http://web.archive.org/web/20220123031752/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')


def test_jan_2022_20(tweet_id_20, jan_2022_memento_20):
    extracted_contents = getters2022.get_jun_2022(jan_2022_memento_20)
    assert extracted_contents == tweet_id_20