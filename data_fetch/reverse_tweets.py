import datetime
import json
import re



def extract_tweet(tweet):
    media_urls = []
    if tweet.has_key('extended_entities') and tweet['extended_entities'].has_key('media'):
      for media in tweet['extended_entities']['media']:
          media_urls.append(media['media_url'])

    text = ''
    date = ''
    exp = re.split(r'^([0-9]?[0-9]/[0-9]?[0-9]/\d\d\d\d)[\s|:]\s*(.+)', tweet['full_text'])
    print tweet['full_text']
    print exp
    if len(exp) > 1:
        text = exp[2]
        date = datetime.datetime.strptime(exp[1], '%d/%m/%Y').isoformat()
    else:
        text = exp[0]

    return {'text': text, 'media': media_urls, 'date' : date}


with open('all_tweets.json') as tweets:
    all_tweets = json.loads(tweets.read())
    reverse_tweets = reversed(all_tweets)
    result_tweets = []

    for tweet in reverse_tweets:
        result_tweets.append(extract_tweet(tweet))

    f = open('reversed_tweets.json', 'w')
    f.write(json.dumps(result_tweets))
    f.close()
