import tweepy
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

api_key = config["twitter_api"]["api_key"]
api_key_secret = config["twitter_api"]["api_key_secret"]
access_token = config["twitter_api"]["access_token"]
access_token_secret = config["twitter_api"]["access_token_secret"]

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)
