from datetime import datetime
from bs4 import BeautifulSoup
import re

def resolve(s):
    """
    Helper function to resolve dates with letters, i.e, 1st, 2nd, 3rd
    """
    return re.sub(r"(\d)(st|nd|rd|th)", r"\1", s)


def get_nov_2008_info(content: BeautifulSoup) -> dict:
    """
    Extract all available info from a tweet with structure from around November 2008
    
    Parameters
    ----------
    content: BeautifulSoup
        A BeautifulSoup object with the parsed content of a Tweet URI-M from around this time frame

    Returns
    ----------
    dict
        Dictionary containing all available information. At most, keys include the following:
        tweet-text: The tweet body
        full-name: Full name of the tweet author
        handle: Twitter handle of the tweet author
        date: datetime of the date the tweet was made

    """

    full_tweet_structure = content.find("div", "desc")

    info = {}
    info['tweet-text'] = full_tweet_structure.find("div", "desc-inner").p.contents[0].get_text().strip()
    info['full-name'] = full_tweet_structure.find("div", "full-name").get_text().strip()
    info['handle'] = full_tweet_structure.find("div", "screen-name").a.contents[0].get_text().strip()

    time = full_tweet_structure.find("span", "entry-meta").get_text().strip().split('\n')[0]
    datetime_object = datetime.strptime(time, "%I:%M %p %B %d, %Y").replace(hour=0, minute=0)
    info['date'] = datetime_object

    return info

def get_dec_2008_info(content: BeautifulSoup) -> dict:
    """
    Extract all available info from a tweet with structure from around November 2009
    
    Parameters
    ----------
    content: BeautifulSoup
        A BeautifulSoup object with the parsed content of a Tweet URI-M from around this time frame

    Returns
    ----------
    dict
        Dictionary containing all available information. At most, keys include the following:
        tweet-text: The tweet body
        full-name: Full name of the tweet author
        handle: Twitter handle of the tweet author
        date: datetime of the date the tweet was made

    """

    full_tweet_structure = content.find("div", "wrapper")

    info = {}
    info['tweet-text'] = full_tweet_structure.find("span", "entry-content").get_text().strip()
    info['full-name'] = full_tweet_structure.find("div", "full-name").get_text().strip()
    if not full_tweet_structure.find("a", "tweet-url screen-name"):
        info['handle'] = full_tweet_structure.find("div", "screen-name").a.contents[0].get_text().strip()
    else:
        info['handle'] = full_tweet_structure.find("a", "tweet-url screen-name").get_text().strip()
    
    try:
        timestamp = full_tweet_structure.find("span", "published")['data']
        timestamp_object = datetime.strptime(timestamp, "{time:'%a %b %d %H:%M:%S %z %Y'}").replace(tzinfo=None, second=0, hour=0, minute=0)
        info['date'] = timestamp_object
    except KeyError:
        timestamp = full_tweet_structure.find("span", "published").get_text().strip()
        timestamp_object = datetime.strptime(resolve(timestamp), "%I:%M %p %b %d, %Y").replace(tzinfo=None, second=0, hour=0, minute=0)
        info['date'] = timestamp_object
    

    # print(info)

    return info

