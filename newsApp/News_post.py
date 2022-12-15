import pandas as pd
import os
from smart_open import smart_open
from twitter import *
import tweepy
from tweepy.auth import OAuthHandler

def news_post():
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    token = os.environ["TOKEN"]
    token_secret = os.environ["TOKEN_SECRET"]
    t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
    news_id = pd.read_csv(smart_open("s3://projecttwitterbot/emotion/send_news_id.csv"), lineterminator='\n')
    news = pd.read_csv(smart_open("s3://projecttwitterbot/emotion/news_emotion.csv"), lineterminator='\n')
    news = news.dropna()
    news_id = news_id.dropna()
    send_news = []
    
    for i in range(len(news[0:25])):
        try:
            news_text = news['title'][i]
            news_path = news['url'][i]
            # check if the news['id'] is already in the news_id['id']
            # last_news_post = int(news['id'][i]) in news_id['id'].unique()
            if news['id'][i] in news_id['id'].unique():
                continue
            else:
                text = news_text + " " + news_path
                api.update_status(text) 
                # record the news that has been sent
                send_news.append(news['id'][i])

        except:
            print("duplicate")
    
        
    send_news_df = pd.DataFrame(send_news)
    send_news_df.rename(columns = {0:'id'}, inplace = True)
    news_df = pd.concat([news_id, send_news_df]).drop_duplicates().reset_index(drop= True)
    news_df.to_csv("s3://projecttwitterbot/emotion/send_news_id.csv", index=False)
        
if __name__ in "__main__":
    news_post()
