# tweet-memento-scraper  
Command line tools for scraping relevant info from Twitter status and profile URLs from archives, regardless of time of archival.

## Usage

### Installing the tools locally with git  
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

### Using the tools for a single uri  
Use the scrape_tweet_memento command for scraping a single given status URI.
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

Use the scrape_profile_memento command for scraping a single given profile URI.  
```
~/scrape_profile_memento https://web.archive.org/web/20090101113614/twitter.com/jack
```   
The above command should produce the following JSON content in a file named output.json  
```
{
   "handle": "jack",
   "full-name": "Jack Dorsey",
   "tweets": [
      {
         "text": "Happy New Year, Twitter.",
         "date": "about 4 hours ago"
      },
      {
         "text": "In a winebago.",
         "date": "about 5 hours ago"
      },
      {
         "text": "Champagne tasting on the roof",
         "date": "about 7 hours ago"
      },
      {
         "text": "Good day to pick up my champagne of the month club.  4 bottles to add to the 17.",
         "date": "about 12 hours ago"
      },
      {
         "text": "NYE 2007, Twitter was young, & I stayed home with a fever as I watched a daemon I wrote send New Year's nudges around the world at midnight.",
         "date": "about 17 hours ago"
      },
      {
         "text": "Hello, San Francisco.",
         "date": "2008-12-30T17:49:00"
      },
      {
         "text": "Headed to the airport after breakfast at grandma's",
         "date": "2008-12-30T06:27:00"
      },
      {
         "text": "There's an entire universe in the smallest of things, even those mundane. I need a haircut.",
         "date": "2008-12-29T18:54:00"
      },
      .
      .
      .
      Full list of tweets redacted, usually returns up to 20 tweets
   ]
   "archived-at": "2009-01-01T11:36:14"
}
```
### Using the tools for multiple URIs in a text file  
Use the scrape_tweet_mementos command for scraping status URIs given in a text file delimited with white space  
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
Use the scrape_profile_mementos command for scraping status URIs given in a text file delimited with white space  
```  
~/scrape_profile_mementos profile_sample.txt   
```
By default, these commands will wait 5 seconds between requests to ease the load on the Wayback Machine and to reduce the number of connection refusals. To change the number of seconds to wait between requests, use the w (waittime) flag like so  
```
scrape_tweet_mementos sample.txt -w 10
```  
This will change the wait time between requests to 10 seconds  

If you wish to bypass the wait between requests entirely, then the f (fast) flag can be used.  
```
scrape_tweet_mementos sample.txt -f
```  
This makes every request sequentially without waiting. This should only be done if you only have about 10 or so URIs to scrape, otherwise you will likely run into connection refusals that could last several minutes.

Both commands support changing of output file name with the -o flag, like below  
```
scrape_tweet_memento http://web.archive.org/web/20170409141941/https://twitter.com/jack/status/20 -o some_other_file.json  
```   

## Notes of known issues  
- In some situations and timeframes, only relative timestamps are available (e.g., 4 hours ago) so these timestamps are left alone, as an ISO format absolute timestamp cannot be created. This is also the case for absolute timestamps that are unknown (let me know about these and I can easily correct for this).
- 