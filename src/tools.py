from datetime import datetime
from bs4 import BeautifulSoup

def get_memento_datetime(memento_datetime_header: str) -> datetime:
    """
    Extract appropriate datetime from Memento datetime header
    """

    return datetime.strptime(memento_datetime_header, "%a, %d %b %Y %H:%M:%S GMT")

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
