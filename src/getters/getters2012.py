from datetime import datetime
from dateutil.parser import parse
from bs4 import BeautifulSoup

def validate_date(date_string: str) -> datetime | None:
    """
    Attempt to validate the timestamp extracted from the page and return it as a datetime
    Can only try against time formats that I know about, so if none match, then None will be returned
    """
    formats = [
        "%I:%M %p - %d %b %y",
        "%I:%M %p - %d %b %Y",
        "%I:%M - %d %b %Y"
    ]
    date = None
    for format in formats:
        try:
            date = datetime.strptime(date_string, format).replace(hour=0, minute=0)
            break
        except ValueError as er:
            print(er)
            continue
    return date

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

    if content.find("div", "components-middle"):
        full_tweet_structure = content.find("div", "components-middle")
    else:
        full_tweet_structure = content.find("div", "permalink-tweet-container")

    info = {}
    info['tweet-text'] = full_tweet_structure.find("p", "js-tweet-text tweet-text").get_text().strip()
    info['handle'] = full_tweet_structure.find("span", "username js-action-profile-name").b.contents[0].get_text().strip()


    fullname_tag = full_tweet_structure.find("strong", "fullname js-action-profile-name show-popup-with-id")
    if fullname_tag.findChild():
        fullname_tag.findChild().clear()
    info['full-name'] = fullname_tag.get_text().strip()

    time = full_tweet_structure.find("span", "metadata").span.contents[0].get_text().strip()
    date = validate_date(time)
    if date:
        info['date'] = date
    else:
        info['date'] = time
    # try:
    #     info['date'] = datetime.strptime(time, "%I:%M %p - %d %b %y").replace(hour=0, minute=0)
    # except ValueError:
    #     info['date'] = datetime.strptime(time, "%I:%M %p - %d %b %Y").replace(hour=0, minute=0)

    return info
