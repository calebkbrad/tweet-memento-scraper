from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_jun_2022(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa June 26 2022 to 

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
    name_plus_handle = content.find("div", {"data-testid": "UserName"}).text.strip().split('@')
    info['full-name'] = name_plus_handle[0]
    info['handle'] = name_plus_handle[1]
    tweets = []
    tweet_list = content.find_all("div", "css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu")
    for tweet in tweet_list:
        author = tweet.find("div", {"data-testid": "User-Names"})
        tweet_text = tweet.find("div", {"data-testid": "tweetText"})
        # print(author.text)
        if author and author.text.strip().split('@')[0] != info['full-name']:
            continue
        if not tweet_text:
            continue
        tweet_info = {}
        tweet_info['text'] = tweet_text.text.strip()
        tweet_info['date'] = tweet.find("time")['datetime']
        # tweet_info['date'] = tweet.find("a", "tweet-timestamp")['title']
        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info