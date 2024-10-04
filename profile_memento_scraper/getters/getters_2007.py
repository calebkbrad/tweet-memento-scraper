from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_aug_2007(content: BeautifulSoup) -> dict:
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
    about = content.find("div", {"id": "side"})
    if content.find("div", "msg"):
        info['handle'] = content.find("div", "msg").strong.text.strip()
    else:
        info['handle'] = content.find("h2", "thumb").text.strip()
    if about.find("span", "fn"):
        info['full-name'] = content.find("span", "fn").text.strip()
    else:
        if 'Name:' in about.text:
            info['full-name'] = about.find("ul", "about").li.text.split("Name: ")[1]
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
        tweet_info = {}
        tweet_info['text'] = tweet.find("span", "entry-title").text.strip()
        tweet_info['date'] = tweet.find("abbr").text.strip()
        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info
