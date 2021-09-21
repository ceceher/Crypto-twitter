import os  
from dotenv import load_dotenv
import tweepy as tw
import pandas as pd
import time

load_dotenv('.env')

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tw.API(auth, wait_on_rate_limit = True)

new_search = "#bitcoin OR #btc OR satoshi -filter:retweets"

# tweets = tw.Cursor(api.search,
#                 q = new_search,
#                 lang = 'en',
#                 since = '2015-01-01').items(100)

tweets = []

for tweet in tw.Cursor(api.search,
                q = new_search,
                count = 100,
                lang = 'en',
                since = '2021-01-01').items():
                tweets.append(tweet)
                users_data = [[tweet.created_at,
                tweet.user.screen_name, 
                tweet.user.name, 
                tweet.user.verified,
                tweet.user.created_at,
                tweet.user.followers_count, 
                tweet.user.friends_count,
                tweet.text] for tweet in tweets]

                tweet_data = pd.DataFrame(data = users_data, 
                    columns=["tweet date", "user", "name", "verified", "user created at", "followers", "following", "text"])
                #print(tweet_data)

                tweet_data.to_csv(path_or_buf = "data.csv")
                time.sleep(2)





