from getters import getters2012
import datetime
import pytest
import requests
from bs4 import BeautifulSoup

@pytest.fixture
def tweet_id_20_after_august():
    return {
        'tweet-text': "just setting up my twttr",
        'full-name': "Jack",
        'handle': "jack",
        'date': datetime.datetime(2006, 3, 21)
    }

@pytest.fixture
def tweet_id_20_with_emoji():
    return {
        'tweet-text': "just setting up my twttr",
        'full-name': "jack",
        'handle': "jack",
        'date': datetime.datetime(2006, 3, 21)
    }


@pytest.fixture
def jan_2016_memento_20():
    url = "http://web.archive.org/web/20160122063429/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def mar_2016_memento_20():
    url = "http://web.archive.org/web/20160311155857/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jul_2016_memento_20():
    url = "http://web.archive.org/web/20160711210454/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def dec_2016_memento_20_with_emoji():
    url = "http://web.archive.org/web/20161225212956/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def aug_2017_memento_20():
    url = "http://web.archive.org/web/20170819200046/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def dec_2017_memento_20():
    url = "http://web.archive.org/web/20171229102850/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def mar_2018_memento_20():
    url = "http://web.archive.org/web/20180403131700/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')


def test_jan_2016_20(tweet_id_20_after_august, jan_2016_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(jan_2016_memento_20)
    assert extracted_contents == tweet_id_20_after_august

def test_mar_2016_20(tweet_id_20_after_august, mar_2016_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(mar_2016_memento_20)
    assert extracted_contents == tweet_id_20_after_august

def test_jul_2016_20(tweet_id_20_after_august, jul_2016_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(jul_2016_memento_20)
    assert extracted_contents == tweet_id_20_after_august

def test_dec_2016_20_with_emoji(tweet_id_20_with_emoji, dec_2016_memento_20_with_emoji):
    extracted_contents = getters2012.get_may_2012_to_may_2022(dec_2016_memento_20_with_emoji)
    assert extracted_contents == tweet_id_20_with_emoji

def test_aug_2017_20(tweet_id_20_with_emoji, aug_2017_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(aug_2017_memento_20)
    assert extracted_contents == tweet_id_20_with_emoji

def test_dec_2017_20(tweet_id_20_with_emoji, dec_2017_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(dec_2017_memento_20)
    assert extracted_contents == tweet_id_20_with_emoji

def test_mar_2018_20(tweet_id_20_with_emoji, mar_2018_memento_20):
    extracted_contents = getters2012.get_may_2012_to_may_2022(mar_2018_memento_20)
    assert extracted_contents == tweet_id_20_with_emoji
