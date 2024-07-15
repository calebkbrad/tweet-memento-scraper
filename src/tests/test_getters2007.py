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
def tweet_id_5310542():
    return {
        'tweet-text': "If you get this message, Twitter has moved to a flock of new servers, each named after a mythical bird. BIG thanks to Jeremy+Blaine for making it happen!",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2007, 2, 4)
    }

@pytest.fixture
def tweet_id_8639931():
    return {
        'tweet-text': "Feeling the weight of staying out late.",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2007, 3, 16)
    }

@pytest.fixture
def tweet_id_42346422():
    return {
        'tweet-text': "Heading (slowly) to OAK airport: STL via PHX. Drowsily thinking about many things.",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2007, 4, 27)
    }

@pytest.fixture
def tweet_id_75841592():
    return {
        'tweet-text': "Be slow w the things that matter. & be fast 2 get there.",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2007, 5, 23)
    }

@pytest.fixture
def tweet_id_67588892():
    return {
        'tweet-text': "Learning lots of tiny mistakes yesterday created a huge outage. Working in earnest to avoid this in the future. Thx for your patience!",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2007, 5, 17)
    }

@pytest.fixture
def tweet_id_479117922():
    return {
        'tweet-text': "Happy Birthday to Gayatri!",
        'full-name': "Jack Dorsey",
        'handle': "jack",
        'date': datetime.datetime(2007, 12, 7)
    }

@pytest.fixture
def feb_2007_memento_5254943():
    url = "http://web.archive.org/web/20070218034409/twitter.com/jack/statuses/5254943"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def feb_2007_memento_5310542():
    url = "http://web.archive.org/web/20070218034419/twitter.com/jack/statuses/5310542"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def mar_2007_memento_8639931():
    url = "http://web.archive.org/web/20070320080129/twitter.com/jack/statuses/8639931"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def may_2007_memento_42346422():
    url = "http://web.archive.org/web/20070519224106/twitter.com/jack/statuses/42346422"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def jul_2007_memento_75841592():
    url = "http://web.archive.org/web/20070703013253/twitter.com/jack/statuses/75841592"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def oct_2007_memento_67588892():
    url = "http://web.archive.org/web/20071008092630/twitter.com/jack/statuses/67588892"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

@pytest.fixture
def dec_2007_memento_479117922():
    url = "http://web.archive.org/web/20071215011930/twitter.com/jack/statuses/479117922"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')



def test_feb_2007_5310542(tweet_id_5310542, feb_2007_memento_5310542):
    extracted_contents = getters2007.get_feb_2007(feb_2007_memento_5310542)
    assert extracted_contents == tweet_id_5310542

def test_feb_2007_5254943(tweet_id_5254943, feb_2007_memento_5254943):
    extracted_contents = getters2007.get_feb_2007(feb_2007_memento_5254943)
    assert extracted_contents == tweet_id_5254943

def test_mar_2007_8639931(tweet_id_8639931, mar_2007_memento_8639931):
    extracted_contents = getters2007.get_feb_2007(mar_2007_memento_8639931)
    assert extracted_contents == tweet_id_8639931

def test_may_2007_42346422(tweet_id_42346422, may_2007_memento_42346422):
    extracted_contents = getters2007.get_feb_2007(may_2007_memento_42346422)
    assert extracted_contents == tweet_id_42346422

def test_jul_2007_75841592(tweet_id_75841592, jul_2007_memento_75841592):
    extracted_contents = getters2007.get_feb_2007(jul_2007_memento_75841592)
    assert extracted_contents == tweet_id_75841592

def test_oct_2007_67588892(tweet_id_67588892, oct_2007_memento_67588892):
    extracted_contents = getters2007.get_feb_2007(oct_2007_memento_67588892)
    assert extracted_contents == tweet_id_67588892

def test_dec_2007_479117922(tweet_id_479117922, dec_2007_memento_479117922):
    extracted_contents = getters2007.get_feb_2007(dec_2007_memento_479117922)
    assert extracted_contents == tweet_id_479117922
