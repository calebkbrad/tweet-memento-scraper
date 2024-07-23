from datetime import datetime
from bs4 import BeautifulSoup

def get_jun_2022(content: BeautifulSoup) -> dict:
    """
    Extract all available info from a tweet with structure from around 2022
    
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
    # print(content)
    full_tweet_structure = content.find(attrs={"role": "region"})

    info = {}
    info['tweet-text'] = full_tweet_structure.find("div", itemprop="articleBody").get_text().strip()
    info['full-name'] = full_tweet_structure.find("meta", itemprop="givenName")['content']
    info['handle'] = full_tweet_structure.find("meta", itemprop="additionalName")['content']
    timestamp = full_tweet_structure.find("meta", itemprop="datePublished")['content']
    info['date'] = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").replace(second=0, minute=0, hour=0)

    return info