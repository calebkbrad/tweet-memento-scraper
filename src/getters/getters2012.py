from datetime import datetime
from bs4 import BeautifulSoup

def get_jun_2012(content: BeautifulSoup) -> dict:
    """
    Extract all available info from a tweet with structure from around June 2012
    
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

    full_tweet_structure = content.find("div", "components-middle")

    info = {}
    info['tweet-text'] = full_tweet_structure.find("p", "js-tweet-text tweet-text").get_text().strip()
    info['handle'] = full_tweet_structure.find("span", "username js-action-profile-name").b.contents[0].get_text().strip()
    info['full-name'] = full_tweet_structure.find("strong", "fullname js-action-profile-name show-popup-with-id").get_text().strip()

    time = full_tweet_structure.find("span", "metadata").span.contents[0].get_text().strip()
    info['date'] = datetime.strptime(time, "%I:%M %p - %d %b %y").replace(hour=0, minute=0)

    return info
