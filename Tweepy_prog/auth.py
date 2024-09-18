import tweepy
import os


def authenticate_twitter_app():
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
