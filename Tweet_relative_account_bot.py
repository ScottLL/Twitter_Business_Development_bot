import base64
import tweepy as twitter
import time, datetime

def twitter_account_bot(user_name):
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    Bearer_Token = os.environ['BEARER_TOKEN'] 
    token = os.environ['TOKEN'] 
    token_secret = os.environ['TOKEN_SECRET'] 

    auth = twitter.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = twitter.API(auth)

    while True:
        print(f"\n{datetime.datetime.now()}\n")
        for tweet in twitter.Cursor(api.search_tweets, q = user_name, count = 10).items(5):
          try: 
              tweet_id = dict(tweet._json)['id']
              tweet_text = dict(tweet._json)['text']

              print('id: ' + str(tweet_id))
              print('text: ' + str(tweet_text))

              api.retweet(tweet_id)

          except twitter.TweepyException as error:
              print(error)
        delay = 30
        time.sleep(delay)
            
            
if __name__ in "__main__":
  user_name = ['MEXC_Global', 'MEXC_Eilla','MEXC_VIP','MEXCDerivatives','EtfMexc','MEXC_SEA','MEXC_Fans','MEXC_CEO']
  for i in range(len(user_name)):
    twitter_account_bot(i)
