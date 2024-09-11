import click
import json
from requests.adapters import HTTPAdapter, Retry
from requests import Session
from . import tools


@click.command()
def cli():
    """
    Click test
    """
    click.echo("This is just a test")

@click.command()
@click.argument("uri")
@click.option("-o", "--output", type=click.File("w"), default="output.json", help="name of desired output file. Default is output.json")
def scrape_tweet_memento(uri: str, output:click.File):
    """
    Scrape the URI-R given by URI argument
    """
    tweet = {}
    try:
        tweet = tools.scrape_single_tweet(uri)
    except Exception as e:
        tweet = {"Error": {repr(e)}}
    json.dump(tweet, output, indent=3)
    

@click.command()
@click.argument("uri_list", type=click.File())
@click.option("-o", "--output", type=click.File("w"), default="output.json", help="name of desired output file. Default is output.json")
@click.option("-f", "--fast", is_flag=True, show_default=True, default=False, help="turn on fast mode, where no effort is made to space out requests. Use only if getting around 10 URIs or less or risk connection refusals for several minutes")
@click.option("-w", "--waittime", type=float, show_default=True, default=5, help="number of seconds to wait between requests when fast mode is not in use")
def scrape_tweet_mementos(uri_list: click.File, output: click.File, fast: bool, waittime: float):
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

    retries = Retry(total=20, connect=20, backoff_factor=10, backoff_max=180)
    session = Session()
    session.mount("https://", HTTPAdapter(max_retries=retries))
    session.mount("http://", HTTPAdapter(max_retries=retries))

    for uri in raw_uris:
        try:
            to_write[uri] = tools.scrape_tweet(uri, session, fast, wait_time=waittime)
        except Exception as e:
            to_write[uri] = {"Error": {repr(e)}}
    
    json.dump(to_write, output, indent=3)