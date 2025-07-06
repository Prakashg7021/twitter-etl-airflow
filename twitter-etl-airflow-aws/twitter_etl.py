# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 16:20:49 2025

@author: PrakashGupta
"""
import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():
    # --------------------------
    # Twitter API credentials
    # --------------------------
    access_key = "" 
    access_secret = "" 
    consumer_key = ""
    consumer_secret = ""


    # --------------------------
    # Authenticate
    # --------------------------
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)
    # --------------------------
    # Extract tweets
    # --------------------------
    tweets = api.user_timeline(screen_name='@elonmusk', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )

    list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        list.append(refined_tweet)

     # --------------------------
    # Create DataFrame
    # --------------------------
    df = pd.DataFrame(list)
     # --------------------------
    # Save to S3
    # --------------------------
    # Make sure you run `aws configure` before using this
    # Install s3fs: pip install s3fs
    df.to_csv("s3://prakashgupta/refined_tweets/elonmusk_tweets.csv", index=False)
