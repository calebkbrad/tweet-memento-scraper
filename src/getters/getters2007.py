from datetime import datetime
from bs4 import BeautifulSoup

def get_feb_2007(content: BeautifulSoup) -> dict:
    """
    Extract all available info from a tweet with structure from around February 2007 (currently the oldest memento I have seen)
    
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
    info['tweet-text'] = full_tweet_structure.find("div", "desc").p.get_text().strip()
    link = full_tweet_structure.find("h2", "thumb").a.find_next_sibling()
    info['full-name'] = link.get_text().strip()
    info['handle'] = link['href'].split('twitter.com/')[1]

    timestamp = full_tweet_structure.find("span", "meta").get_text().strip().split('\n')[0]
    info['date'] = datetime.strptime(timestamp, "%I:%M %p %B %d, %Y").replace(hour=0, minute=0)
    
    return info