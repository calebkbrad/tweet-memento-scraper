#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup

def main(args):
    try:
        url = args[0]
    except IndexError:
        print("Please enter a url")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())

    

if __name__ == "__main__":
    main(sys.argv[1:])