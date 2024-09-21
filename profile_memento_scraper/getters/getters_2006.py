from datetime import datetime
from bs4 import BeautifulSoup
import string

def get_profile_nov_2006(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa  Nov/early Dec 2006.

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
    # For stripping white space
    whitespace_except_space = string.whitespace.replace(" ", "")
    about = content.find("div", {"id": "side"})
    info['handle'] = content.title.text.split("/ ")[1]
    if 'Name:' in about.text:
        info['full-name'] = about.find("ul", "about").find("ui").text.split("Name: ")[1]
    else:
        info['full-name'] = "Name not available"

    tweets = []
    latest_tweet = {}
    current_tweet = content.find("div", "desc")
    latest_tweet['text'] = current_tweet.p.text.strip()
    latest_tweet['date'] = current_tweet.a.text.strip()
    tweets.append(latest_tweet)
    tweet_list = content.find("table", "doing").find_all("tr")
    for tweet in tweet_list:
        # last tr is potentially empty, ignore it if it is
        if not tweet.get("class"):
            continue
        tweet_info = {}
        date = tweet.find("span", "meta")
        if date:
            tweet_info['date'] = date.text.strip().split("\n")[0]
            date.clear()
        else:
            date = tweet.find("p", "meta")
            tweet_info['date'] = date.text.strip().split("\n")[0]
            date.clear()
        tweet.find("span", "meta").clear()
        if tweet.td.get("class"):
            tweet.td.extract()
        tweet_info['text'] = tweet.td.text.strip()
        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info
