# Twitter_Bots
[![Python main_new_coin.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_new_coin.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_new_coin.yml)

[![Python main_old_coin.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_old_coin.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_old_coin.yml)

[![Python News_df.py](https://github.com/ScottLL/Twitter_Business_Development_bot/actions/workflows/News_searching_bot.yml/badge.svg?branch=main)](https://github.com/ScottLL/Twitter_Business_Development_bot/actions/workflows/News_searching_bot.yml)

[![Python Tweet_relative_account_bot.py](https://github.com/ScottLL/Twitter_Business_Development_bot/actions/workflows/Tweet_relative_account_bot_main.yml/badge.svg?branch=main)](https://github.com/ScottLL/Twitter_Business_Development_bot/actions/workflows/Tweet_relative_account_bot_main.yml)

[![Python GPT-3_twits.py](https://github.com/ScottLL/Twitter_Business_Development_bot/actions/workflows/retwitter.yml/badge.svg?branch=main)](https://github.com/ScottLL/Twitter_Business_Development_bot/actions/workflows/retwitter.yml)

## Project Description
The project is for IDS 706 Data Engineering class at Duke University. The goal is to build a Microservice that performs a query using CI/CD, Python, SQL or Dask/Spark and returns useful information to users. Our team created a series of Twitter bots to automate the process of soliciting business for entrepreneurs or start-ups with limited marketing budgets. 

### Bot solution for business development
The ideas, projects, and actions that improve a business can be summed up as business development. This entails raising sales, expanding the business, improving profitability through forming strategic alliances, and making strategic business choices. In this project, we are building a bot to help the business run the Twitter account and reach out to the target user by sending them direct messages. 

Benefits:
1. Twitter bot help businesses reach out the more target audients and run the account automatically. 
2. It can help businesses save time and employ costs to develop business. 
3. Provide the public with a positive reputation for the business.
4. Get real followers in a short time. 

## Project Sponsor
This project is sponsored by MEXC Global exchange, so we are run the bot with MEXC Twitter account. 

**MEXC Global Exchange** is a centralized exchange that employs a high-performance mega-transaction matching technology. The CEX platform is run by a team of professionals with extensive financial industries and blockchain technology experience. Currently, MEXC Global has around 5 million users in more than 70 countries around the world.

## Data Flow Diagram

<img width="802" alt="Screen Shot 2022-12-14 at 10 48 23 AM" src="https://user-images.githubusercontent.com/105904149/207643223-6f9427b8-cd5c-4494-b354-84ae22017586.png">

`searching_tweets.py`: searches for tweets every 15 minutes and adds new tweets to a csv file stored in an AWS S3 bucket.

`direct_messages.py`: sends 500 messages per day to twitter influencers with more than 300 and less than 20,000 followers, using information in the .csv file from AWS S3 bucket.

`tweet_relative_account_bot.py`: retweets content based on popularity every 15 minutes.

`retwitter_content_bot.py`: retweets content based on google searching keywords in google sheet.

`News_df.py` : retrieves crypto news updates from CryptoPanic.com.

`News_post.py` : posts news updates to twitter.


## Demo Video
[Twitter Bots for Business Development](https://youtu.be/DA69OHjqZ10)
