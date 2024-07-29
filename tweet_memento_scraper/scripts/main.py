import click
import json
from . import tools


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
    \b
    Scrape the URI-Rs in the URI_LIST text file. 
    URI_LIST text file should contain URI-Rs separated by white space
    Results are dumped to output file in JSON with the following schema, labelled by URI:
        tweet-text: The tweet body
        full-name: Full name of the tweet author
        handle: Twitter handle of the tweet author
        date: datetime of the date the tweet was made in iso. This field truncates precision from hour onwards
        archived-at: datetime of the date the memento was archived in iso
    """
    raw_uris = uri_list.read().split()
    to_write = {}

    for uri in raw_uris:
        to_write[uri] = tools.scrape_tweet(uri)
    
    json.dump(to_write, output, indent=3)