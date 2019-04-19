Utilities to extract and reverse the set of tweets that will feed the app with data.

To run: 
1) Install the tweepy api (http://docs.tweepy.org/en/v3.5.0/api.html).
2) Geta a API Key set from twitter (https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)
3) Create a config.json file with the following structure
{                                                                               
  "consumer_key": "",                                  
  "consumer_secret": "",      
  "access_token": "",         
  "access_token_secret": ""        
}  



4) Run: python fetch_tweets.py
This will geneate a file with all the tweets named all_tweets.json

5) Run: python reverse_tweets.py

This will generate a file called reversed_tweets.json with the tweets in reverse order and with only the information required for display (as opposed to all_tweets.json which contains all the information returned by the tweepy API)
