import click
import json
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

@click.command()
@click.argument("uri_list", type=click.File())
@click.option("-o", "--output", type=click.File("w"), default="output.json", help="name of desired output file. Default is output.json")
def scrape_tweet_mementos(uri_list: click.File, output: click.File):
    """
    Scrape the URI-Rs in the URI_LIST text file. 
    URI_LIST text file should contain URI-Rs separated by white space
    """
    