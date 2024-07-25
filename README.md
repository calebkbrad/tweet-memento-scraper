# tweet-memento-scraper  
A command line tool for scraping a Twitter status URI-M for info about that tweet  

## Usage

## Installing the tool locally with git  
1. Setup venv (optional but I would recommend it)
   1. Create venv
   ```
   ~/python3 -m venv /insert/desired/path/here
   ~/cd /insert/desired/path/here
   ```
   2. Activate venv
   ```
   source bin/activate
   ```
2. Clone the repo
   ```
    ~/git clone git@github.com:calebkbrad/tweet-memento-scraper.git
    ~/cd tweet-memento-scraper
   ```
3. Install with pip
   ```
    ~/pip install --editable .
   ```
4. Run the tool
    ```
    ~/scrape_tweet_mementos --help  
    Usage: scrape_tweet_mementos [OPTIONS] URI_LIST  
    Scrape the URI-Rs in the URI_LIST text file.  
    URI_LIST text file should contain URI-Rs separated by white space  
    Results are dumped to output file in JSON with the following schema:  
        tweet-text: The tweet body  
        full-name: Full name of the tweet author  
        handle: Twitter handle of the tweet author  
        date: datetime of the date the tweet was made in iso. This
        field truncates precision from hour onwards  
        archived-at: datetime of the date the memento was archived in
        iso
        uri: URI-R of the memento  
    Options:
    -o, --output FILENAME  name of desired output file. Default is output.json
    --help                 Show this message and exit.  
