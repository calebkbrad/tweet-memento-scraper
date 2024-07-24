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

@click.command()
@click.argument("uri")
def scrape_tweet_memento(uri: str):
    """
    Scrape the URI-R given by URI argument
    """
    print(tools.scrape_tweet(uri))
