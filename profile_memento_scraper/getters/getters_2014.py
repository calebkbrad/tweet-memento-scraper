from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_may_2014(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa May 2014 to July 2014? (time currently unclear)

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
    info['handle'] = content.find("span", "screen-name").text.strip().split('@')[1]
    info['full-name'] = content.find("span", "profile-field").text.strip()

    tweet_list = content.find_all("div", "content")
    for tweet in tweet_list:
        author = tweet.find("strong", "fullname")
        tweet_text = tweet.find("p", "tweet-text")
        if not author:
            continue
        if author.text.strip() != info['full-name']:
            continue
        if not tweet_text:
            continue
        tweet_info = {}

        tweet_info['text'] = tweet_text.text.strip()
        tweet_info['date'] = tweet.find("small", "time").a['title']
        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info

def get_profile_jul_2014(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa July 2014 to 

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
    info['handle'] = content.find("div", "ProfileCardMini-screenname").text.strip().split('@')[1]
    info['full-name'] = content.find("a", "ProfileHeaderCard-nameLink").text.strip()

    tweet_list = content.find_all("div", {"data-component-term": "tweet"})
    for tweet in tweet_list:
        author = tweet.find("b", "ProfileTweet-fullname")
        tweet_text = tweet.find("p", "js-tweet-text")
        if author and author.text.strip() != info['full-name']:
            continue
        tweet_info = {}

        tweet_info['text'] = tweet_text.text.strip()
        tweet_info['date'] = tweet.find("a", "ProfileTweet-timestamp")['title']
        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info