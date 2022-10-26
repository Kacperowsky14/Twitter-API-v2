import tweepy
import configparser
import pandas as pd # Importing the necessary libraries


config = configparser.ConfigParser()
config.read("config.ini")   # Connecting to the config.imi file

api_key = config["twitter_api"]["api_key"]
api_key_secret = config["twitter_api"]["api_key_secret"]
access_token = config["twitter_api"]["access_token"]
access_token_secret = config["twitter_api"]["access_token_secret"] # With these lines of code I am retrieving the data needed to connect to my developer profil

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret) #Accessing Twitter data using access
api = tweepy.API(auth)      

public_tweets = api.home_timeline() # Retrieving data from a linked profile. To do this, you need to apply to Twitter to upgrade your account status

columns = ["Time" "User" "Tweet"] # selecting columns to download data from Twitter
data = [] 

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text]) # adding data to the data structure, which will allow you to create a dataframe

df = pd.DataFrame(data, columns) # Create a data frame

df.to_csv("twitter_api.csv") # Save dataframe to CSV file