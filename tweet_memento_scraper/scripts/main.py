import click
import bs4
import requests
from . import tools
from .. import getters


@click.command()
def cli():
    """
    Click test
    """
    click.echo("This is just a test")

def scrape_tweet(uri: str) -> dict:
    """
    Scrape the tweet for available info, return as dict
    """
    
    

@click.command()
@click.argument("uri")
def scrape_tweet_memento(uri: str):
    """
    Scrape the URI-R given by URI argument
    """
    print(uri)
