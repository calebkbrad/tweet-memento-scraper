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
def tweet_id_20_after_august():
    return {
        'tweet-text': "just setting up my twttr",
        'full-name': "Jack",
        'handle': "jack",
        'date': datetime.datetime(2006, 3, 21)
    }



@pytest.fixture
def tweet_id_334653979390779392():
    return {
        'tweet-text': "“When you're in jail, a good friend will bail you out. A best friend will be in the cell next to you saying, 'Damn, that was fun'.”―Groucho",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2013, 5, 15)
    }

@pytest.fixture
def tweet_id_398482069279748096():
    return {
        'tweet-text': "A thank you and congratulations to @dickc, @mgupta, @vijaya, @gabrielstricker, and the @Twitter team! $TWTR",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2013, 11, 7)
    }

@pytest.fixture
def tweet_id_415211454720004096_german_withpic():
    return {
        'tweet-text': "“I only hope we don't lose sight of one thing—that it was all started by a mouse.”—Walt Disney pic.twitter.com/MgY9byVIkz",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2013, 12, 23)
    }

@pytest.fixture
def tweet_id_334364760252489728():
    return {
        'tweet-text': "Square is now processing $15 billion annualized. That's without Starbucks included. I couldn't be more proud of our team!",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2013, 5, 14)
    }



@pytest.fixture
def jan_2014_memento_334653979390779392():
    url = "https://web.archive.org/web/20140117171911/twitter.com/jack/status/334653979390779392"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jan_2014_memento_398482069279748096():
    url = "http://web.archive.org/web/20140129112819/twitter.com/jack/status/398482069279748096"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jan_2014_memento_415211454720004096_german_withpic():
    url = "http://web.archive.org/web/20140109183606/twitter.com/jack/status/415211454720004096"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def feb_2014_memento_20():
    url = "http://web.archive.org/web/20140209151232/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def apr_2014_memento_334364760252489728():
    url = "http://web.archive.org/web/20140407201626/twitter.com/jack/status/334364760252489728"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def aug_2015_memento_20():
    url = "http://web.archive.org/web/20150812205308/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def aug_2015_second_half_memento_20():
    url = "http://web.archive.org/web/20150815223546/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def oct_2015_memento_20():
    url = "http://web.archive.org/web/20151002205430/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def nov_2015_memento_20():
    url = "http://web.archive.org/web/20151106063459/twitter.com/jack/status/20"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')



def test_jan_2014_334653979390779392(tweet_id_334653979390779392, jan_2014_memento_334653979390779392):
    extracted_contents = getters2012.get_jun_2012(jan_2014_memento_334653979390779392)
    assert extracted_contents == tweet_id_334653979390779392

def test_jan_2014_398482069279748096(tweet_id_398482069279748096, jan_2014_memento_398482069279748096):
    extracted_contents = getters2012.get_jun_2012(jan_2014_memento_398482069279748096)
    assert extracted_contents == tweet_id_398482069279748096

@pytest.mark.skip(reason="Date is in another language, don't currently know how to deal with this")
def test_jan_2014_415211454720004096_german_withpic(tweet_id_415211454720004096_german_withpic, jan_2014_memento_415211454720004096_german_withpic):
    extracted_contents = getters2012.get_jun_2012(jan_2014_memento_415211454720004096_german_withpic)
    assert extracted_contents == tweet_id_415211454720004096_german_withpic

def test_feb_2014_20(tweet_id_20, feb_2014_memento_20):
    extracted_contents = getters2012.get_jun_2012(feb_2014_memento_20)
    assert extracted_contents == tweet_id_20

def test_apr_2014_334364760252489728(tweet_id_334364760252489728, apr_2014_memento_334364760252489728):
    extracted_contents = getters2012.get_jun_2012(apr_2014_memento_334364760252489728)
    assert extracted_contents == tweet_id_334364760252489728

def test_aug_2015_20(tweet_id_20_after_august, aug_2015_memento_20):
    extracted_contents = getters2012.get_jun_2012(aug_2015_memento_20)
    assert extracted_contents == tweet_id_20_after_august

def test_aug_2015_second_half_20(tweet_id_20_after_august, aug_2015_second_half_memento_20):
    extracted_contents = getters2012.get_jun_2012(aug_2015_second_half_memento_20)
    assert extracted_contents == tweet_id_20_after_august

def test_oct_2015_20(tweet_id_20_after_august, oct_2015_memento_20):
    extracted_contents = getters2012.get_jun_2012(oct_2015_memento_20)
    assert extracted_contents == tweet_id_20_after_august

def test_nov_2015_20(tweet_id_20_after_august, nov_2015_memento_20):
    extracted_contents = getters2012.get_jun_2012(nov_2015_memento_20)
    assert extracted_contents == tweet_id_20_after_august
