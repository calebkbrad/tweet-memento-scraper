import requests
import datetime
from tools import get_memento_datetime

def main(args):
    url = "http://web.archive.org/web/20081103142857/https://twitter.com/jack/status/20"
    response = requests.get(url)
    # print(response.content)
    print(get_memento_datetime(response.headers['memento-datetime']))