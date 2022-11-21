import gspread
from twitter import *
import tweepy
import urllib.request
from tweepy.auth import OAuthHandler
import os


def retwitter_content_bot():

    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    Bearer_Token = os.environ["BEARER_TOKEN"]
    token = os.environ["TOKEN"]
    token_secret = os.environ["TOKEN_SECRET"]

    t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)

    # Open a sheet from a spreadsheet i
    gc = gspread.service_account("credentials.json")
    wks = gc.open("retweet_bot").sheet1

    # Update a range of cells using the top left corner address
    next_tweet = wks.acell("D3").value
    img = wks.acell("G3").value

    length = len(next_tweet)

    if length < 280:
        if img != None:
            path = "/tmp/images.jpg"
            text = next_tweet
            urllib.request.urlretrieve(img, path)
            api.update_status_with_media(text, path)
            # delete row on success
            os.remove("/tmp/images.jpg")
            wks.delete_rows(3)
        else:
            # Update your status
            t.statuses.update(status=next_tweet)
            # delete row on success
            wks.delete_rows(3)

    else:
        wks.delete_rows(3)


if __name__ in "__main__":

    retwitter_content_bot()
