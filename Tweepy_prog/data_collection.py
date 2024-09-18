def fetch_tweets(api, query, count=100):
    tweets = api.search(q=query, count=count, tweet_mode='extended')
    return tweets


def tweets_to_dataframe(tweets):
    import pandas as pd

    data = {
        'created_at': [tweet.created_at for tweet in tweets],
        'text': [tweet.full_text for tweet in tweets],
        'user': [tweet.user.screen_name for tweet in tweets]
    }
    df = pd.DataFrame(data)
    return df
