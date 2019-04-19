import json

with open("all_tweets.json") as tweets:
    all_tweets = json.loads(tweets.read())
    reverse_tweets = reversed(all_tweets)
    result_tweets = []
    for tweet in reverse_tweets:
        media_urls = []
        if tweet.has_key("extended_entities") and tweet["extended_entities"].has_key("media"):
            for media in tweet["extended_entities"]["media"]:
                media_urls.append(media["media_url"])
        result_tweets.append({"text": tweet["full_text"], "media": media_urls})
    f = open("reversed_tweets.json", "w")
    f.write(json.dumps(result_tweets))
    f.close()
