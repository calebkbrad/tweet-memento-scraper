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
def tweet_id_20_second_half():
    return {
        'tweet-text': "just setting up my twttr",
        'full-name': "jack",
        'handle': "jack",
        'date': datetime.datetime(2006, 3, 21)
    }


@pytest.fixture
def jan_2022_memento_20():
    url = "http://web.archive.org/web/20220123031752/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def may_2022_memento_20():
    url = "http://web.archive.org/web/20220506122041/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def aug_2022_memento_20():
    url = "http://web.archive.org/web/20220806082835/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def dec_2022_memento_20():
    url = "http://web.archive.org/web/20221220171620/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def mar_2023_memento_20():
    url = "http://web.archive.org/web/20230307130951/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jul_2023_memento_20():
    url = "http://web.archive.org/web/20230615112336/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def aug_2023_memento_20():
    url = "http://web.archive.org/web/20230816204033/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def sept_2023_memento_20():
    url = "http://web.archive.org/web/20230927120154/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')


def test_jan_2022_20(tweet_id_20, jan_2022_memento_20):
    extracted_contents = getters2022.get_jun_2022(jan_2022_memento_20)
    assert extracted_contents == tweet_id_20

def test_may_2022_20(tweet_id_20, may_2022_memento_20):
    extracted_contents = getters2022.get_jun_2022(may_2022_memento_20)
    assert extracted_contents == tweet_id_20

def test_aug_2022_20(tweet_id_20_second_half, aug_2022_memento_20):
    extracted_contents = getters2022.get_jun_2022(aug_2022_memento_20)
    assert extracted_contents == tweet_id_20_second_half

def test_dec_2022_20(tweet_id_20_second_half, dec_2022_memento_20):
    extracted_contents = getters2022.get_jun_2022(dec_2022_memento_20)
    assert extracted_contents == tweet_id_20_second_half

def test_mar_2023_20(tweet_id_20_second_half, mar_2023_memento_20):
    extracted_contents = getters2022.get_jun_2022(mar_2023_memento_20)
    assert extracted_contents == tweet_id_20_second_half

def test_jul_2023_20(tweet_id_20_second_half, jul_2023_memento_20):
    extracted_contents = getters2022.get_jun_2022(jul_2023_memento_20)
    assert extracted_contents == tweet_id_20_second_half

def test_aug_2023_20(tweet_id_20_second_half, aug_2023_memento_20):
    extracted_contents = getters2022.get_jun_2022(aug_2023_memento_20)
    assert extracted_contents == tweet_id_20_second_half

def test_sept_2023_20(tweet_id_20_second_half, sept_2023_memento_20):
    extracted_contents = getters2022.get_jun_2022(sept_2023_memento_20)
    assert extracted_contents == tweet_id_20_second_half
