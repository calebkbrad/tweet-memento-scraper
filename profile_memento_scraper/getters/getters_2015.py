from datetime import datetime
from bs4 import BeautifulSoup

def get_profile_may_2015(content: BeautifulSoup) -> dict:
    """
    Get a profile's information circa May 29 2015 to 

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
    tweet_list = content.find_all("div", "content")
    print(len(tweet_list))
    for tweet in tweet_list:
        author = tweet.find("strong", "fullname")
        tweet_text = tweet.find("p", "js-tweet-text")
        if author and author.text.strip() != info['full-name']:
            continue
        if not tweet_text:
            continue
        tweet_info = {}
        tweet_info['text'] = tweet_text.text.strip()
        tweet_info['date'] = tweet.find("a", "tweet-timestamp")['title']
        tweets.append(tweet_info)
    info['tweets'] = tweets

    return info