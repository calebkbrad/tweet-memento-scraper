from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_feb_2009(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa August 2008 to .

    Parameters
    ------------
    content: A BeautifulSoup object with the content of a profile page from this timeframe
    
    Returns
    ------------
    dict
        Dictionary containing all available information, including the following:
        handle: The current username of the user
        full-name: The current screen name of the user
    """
    info = {}
    if content.find("div", "msg"):
        info['handle'] = content.find("div", "msg").strong.text.strip()
    elif content.find("h2", "thumb"):
        info['handle'] = content.find("h2", "thumb").text.strip()
    else:
        info['handle'] = content.find("div", {"id":"profiletext"}).strong.text.strip()
    if content.find("span", "fn"):
        info['full-name'] = content.find("span", "fn").text.strip()
    else:
        info['full-name'] = "Name not available"

    tweets = []
    tweet_list = content.find("ol", "statuses").find_all("li")
    for tweet in tweet_list:
        tweet_info = {}
        tweet_info['text'] = tweet.find("span", "entry-content").text.strip()
        tweet_info['date'] = tweet.find("span", "published").text.strip()
        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info
