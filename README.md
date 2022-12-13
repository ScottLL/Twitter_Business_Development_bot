# Twitter_Bots
[![Python main_new_coin.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_new_coin.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_new_coin.yml)

[![Python main_old_coin.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main.yml)

[![Python retwitter_content_bot.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/retwitter_content_bot_main.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/retwitter_content_bot_main.yml)

[![Python Tweet_relative_account_bot.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/Tweet_relative_account_bot_main.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/Tweet_relative_account_bot_main.yml)


## Project Description
The project is for IDS 706 Data Engineering class at Duke University. The goal is to build a Microservice that performs a query using either Pandas, SQL or Dask/Spark and returns useful information to users. Our team created a series of Twitter bots to automate the process of soliciting business for entrepreneurs or start-ups with limited marketing budgets. 

## Data Flow Diagram
![twitter_bots](https://user-images.githubusercontent.com/105904149/207117949-4e53fda5-65a0-483c-87b8-460d34b3ac82.jpeg)

`searching_tweets.py`: searches for tweets every 15 minutes and adds new tweets to a csv file stored in an AWS S3 bucket.

`direct_messages.py`: sends 500 messages per day to English speaking twitter influencers with more than 300 and less than 20,000 followers, using information in the .csv file from AWS S3 bucket.

`tweet_relative_account_bot.py`: retweets content based on popularity every 15 minutes.

`retwitter_content_bot.py`: retweets content based on keywords.

## Demo Video
[Group Project - Twitter Bots]()


## Sample Output

