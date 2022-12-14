import tweepy
import pandas as pd
import os
import time
from smart_open import smart_open

def searchTweets(query, max_results):
    
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    Bearer_Token = os.environ["BEARER_TOKEN"]
    Token = os.environ["TOKEN"]
    Token_Secret = os.environ["TOKEN_SECRET"]
    #     print(len(Token_Secret), "consumer_key: ", len(consumer_key), len(consumer_secret), len(Bearer_Token), len(Token))
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
    secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(Token, Token_Secret)

    getClient = tweepy.Client(
        bearer_token=Bearer_Token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=Token,
        access_token_secret=Token_Secret,
    )
    client = getClient

    search_df = pd.read_csv(smart_open('s3://projecttwitterbot/Searching/search_df.csv'), lineterminator='\n')

    search_df = search_df[search_df.created_at != "topstonks"]
    
    search_df = search_df.drop(columns=["Unnamed: 0"])

    search_df["created_at"] = pd.to_datetime(
       search_df["created_at"], format="%Y-%m-%d %H:%M:%S",
        errors='coerce')

    search_df = search_df.dropna()
    search_df = search_df.astype(
        {
            "id": "int64",
            "verified": "bool",
            "author_id": "int64",
            "followers_count": "int64",
            "following_count": "int64",
            "tweet_count": "int64",
        }
    )

    tweets = client.search_recent_tweets(
        query=query,
        tweet_fields=["id", "text", "context_annotations", "created_at", "lang"],
        expansions=[
            "referenced_tweets.id",
            "attachments.media_keys",
            "author_id",
            "entities.mentions.username",
            "geo.place_id",
        ],
        user_fields=[
            "id",
            "username",
            "description",
            "entities",
            "protected",
            "public_metrics",
            "verified",
        ],
        place_fields=["place_type", "geo"],
        media_fields=[
            "duration_ms",
            "height",
            "media_key",
            "preview_image_url",
            "type",
            "width",
            "url",
            "public_metrics",
        ],
        max_results = max_results
    )

    user = {u["id"]: u for u in tweets.includes["users"]}
    results = []
    if not tweets.data is None and len(tweets.data) > 0:
        for tweet in tweets.data:
            twt = client.get_tweets(
                tweet["id"], expansions=["author_id"], user_fields=["username"]
            )
            obj = {}
            obj["id"] = tweet["id"]
            obj["created_at"] = tweet["created_at"]
            obj["author_id"] = tweet.id
            obj["text"] = tweet.text
            obj["lang"] = tweet.lang
            # obj['entities'] = tweet.entities
            obj["username"] = twt.includes["users"][0].username
            if user[tweet.author_id]:
                user1 = user[tweet.author_id]
                # obj['public_metrics'] = user1.public_metrics
                obj["verified"] = user1.verified

            obj["url"] = "https://twitter.com/{}/status/{}".format(
                twt.includes["users"][0].username, tweet["id"]
            )
            obj["followers_count"] = user1.public_metrics["followers_count"]
            obj["following_count"] = user1.public_metrics["following_count"]
            obj["tweet_count"] = user1.public_metrics["tweet_count"]

            results.append(obj)
    else:
        return "No tweets found"

    search_df_new = pd.DataFrame(results)
    search_df_new["created_at"] = pd.to_datetime(
        search_df_new["created_at"], format="%Y-%m-%d %H:%M:%S"
    )

    # merge the search_df_new with the search_df base on the id
    new_df = pd.merge(
        search_df,
        search_df_new,
        on=[
            "id",
            "created_at",
            "author_id",
            "text",
            "lang",
            "username",
            "verified",
            "url",
            "followers_count",
            "following_count",
            "tweet_count",
        ],
        how="outer",
    )
    new_df["created_at"] = pd.to_datetime(
        new_df["created_at"], format="%Y-%m-%d %H:%M:%S"
    )
    # save the dataframe to s3
    new_df.to_csv(
        "s3://projecttwitterbot/Searching/search_df.csv",
        storage_options={"key": access_key, "secret": secret_access_key})
    return new_df


