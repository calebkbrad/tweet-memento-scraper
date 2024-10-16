from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_dec_2011(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa December 2011 to around May 2012 (unclear).

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
    info['handle'] = content.find("span", "screen-name").text.strip().split("@")[1]
    info['full-name'] = content.find("div", "full-name").h2.text.strip()

    tweets = []
    tweet_list = content.find_all("div", "stream-item")
    for tweet in tweet_list:
        tweet_info = {}
        # If a retweet, skip
        author = tweet.find("a", "tweet-screen-name").text.strip()
        if author != info['handle']:
            continue

        tweet_info['text'] = tweet.find("div", "tweet-text").text.strip()
        tweet_info['date'] = tweet.find("span", "_timestamp")['data-time']

        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info
