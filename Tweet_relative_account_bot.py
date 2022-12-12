import tweepy
import time
import datetime
import os


def twitter_account_bot():
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    token = os.environ["TOKEN"]
    token_secret = os.environ["TOKEN_SECRET"]

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)

    # timeout variable can be omitted, if you use specific value in the while condition
    timeout = 300   # [seconds]

    timeout_start = time.time()
    delay = 30
    time.sleep(delay)
    
    while time.time() < timeout_start + timeout:
            print(f"\n{datetime.datetime.now()}\n")
            user_name = [
                "MEXC_Global",
                "MEXC_Eilla",
                "MEXC_VIP",
                "MEXCDerivatives",
                "EtfMexc",
                "MEXC_SEA",
                "MEXC_Fans",
                "MEXC_CEO",
            ]
            for i in range(len(user_name)):
                var = tweepy.Cursor(
                    api.search_tweets, q=user_name[i], count=20, result_type="popular"
                ).items(10)
                for tweet in var:
                    try:
                        tweet_id = dict(tweet._json)["id"]
                        tweet_text = dict(tweet._json)["text"]

                        print("id: " + str(tweet_id))
                        print("text: " + str(tweet_text))

                        api.retweet(tweet_id)

                    except tweepy.TweepyException as error:
                        print(error)

                delay = 3
                time.sleep(delay)
            break
            
if __name__ in "__main__":
    twitter_account_bot()
