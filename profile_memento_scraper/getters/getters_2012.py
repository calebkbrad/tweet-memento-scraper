from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_may_2012(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa May 2012 to 

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
    tweets = []
    # This time has differing structures, so need different scrapers
    if content.find("div", "screen-name"):
        info['handle'] = content.find("div", "screen-name").text.strip()
        info['full-name'] = content.find("span", "fn").text.strip()

        tweet_list = content.find("ol", "statuses").find_all("li")
        for tweet in tweet_list:
            author = tweet.find("a", "screen-name")
            if author and author.text.strip() != info['handle']:
                continue
            tweet_info = {}
            tweet_info['text'] = tweet.find("span", "entry-content").text.strip()
            tweet_info['date'] = tweet.find("span", "timestamp")['data']
            tweets.append(tweet_info)
    elif content.find("span", "screen-name"):
        info['handle'] = content.find("span", "screen-name").text.strip().split("@")[1]
        info['full-name'] = content.find("h1", "fullname").text.strip()

        tweet_list = content.find_all("div", "content")
        for tweet in tweet_list:
            author = tweet.find("strong", "fullname")
            if author and author.text.strip() != info['full-name']:
                continue
            tweet_info = {}
            tweet_info['text'] = tweet.find("p", "js-tweet-text").text.strip()
            tweet_info['date'] = tweet.find("a", "tweet-timestamp")['title']
            tweets.append(tweet_info)
    info['tweets'] = tweets

    return info
