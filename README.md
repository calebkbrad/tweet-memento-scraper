# tweet-memento-scraper  
A command line tool for scraping a Twitter status URI-M for info about that tweet  

## Usage

### Installing the tool locally with git  
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

### Using the tool for a single uri  
Use the scrape_tweet_memento command for scraping a single given URI.
```
~/scrape_tweet_memento http://web.archive.org/web/20170409141941/https://twitter.com/jack/status/20
```  
The above command should produce the following JSON content in a file named output.json  
```
{
   "tweet-text": "just setting up my twttr",
   "handle": "jack",
   "full-name": "jack",
   "date": "2006-03-21T00:00:00",
   "archived-at": "2017-04-09T14:19:41"
}  
```  
### Using the tool for multiple URIs in a text file  
Use the scrape_tweet_mementos command for scraping URIs given in a text file delimited with white space  
```
scrape_tweet_mementos sample.txt  
```  
The above command (given the sample.txt [here](sample.txt)) should produce the following JSON content in a file named output.json.  
```
{
   "http://web.archive.org/web/20081222104434/https://twitter.com/jack/status/20": {
      "tweet-text": "just setting up my twttr",
      "full-name": "Jack Dorsey",
      "handle": "jack",
      "date": "2006-03-21T00:00:00",
      "archived-at": "2008-12-22T10:44:34"
   },
   "https://web.archive.org/web/20071024130209/http://twitter.com:80/guru/statuses/343504652": {
      "tweet-text": "\"Only those who risk going too far can possibly find out how far one can go.\" [T.S. Elliot] Found on a bottle of *Hard* Pear Cider. Risqu\u00e9.",
      "full-name": "Jacob",
      "handle": "guru",
      "date": "2007-10-17T00:00:00",
      "archived-at": "2007-10-24T13:02:09"
   },
   "http://web.archive.org/web/20090924111048/https://twitter.com/jack/status/968105771": {
      "tweet-text": "\"Don't make something unless it is both necessary and useful; but if it is both, don't hesitate to make it beautiful.\"",
      "full-name": "Jack Dorsey",
      "handle": "jack",
      "date": "2008-10-20T00:00:00",
      "archived-at": "2009-09-24T11:10:48"
   },
   "http://web.archive.org/web/20140109183606/twitter.com/jack/status/415211454720004096": {
      "tweet-text": "\u201cI only hope we don't lose sight of one thing\u2014that it was all started by a mouse.\u201d\u2014Walt Disney pic.twitter.com/MgY9byVIkz",
      "handle": "jack",
      "full-name": "Jack Dorsey",
      "date": "2013-12-23T00:00:00",
      "archived-at": "2014-01-09T18:36:06"
   }
}
```  
Both commands support changing of output file name with the -o flag, like below  
```
scrape_tweet_memento http://web.archive.org/web/20170409141941/https://twitter.com/jack/status/20 -o some_other_file.json  
```