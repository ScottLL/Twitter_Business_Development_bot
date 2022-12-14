# Twitter_Bots
[![Python main_new_coin.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_new_coin.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_new_coin.yml)

[![Python main_old_coin.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_old_coin.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/main_old_coin.yml)

[![Python newsApp/News_df.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/News_searching_bot.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/News_searching_bot.yml)

[![Python newsApp/News_post.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/News_post.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/News_post.yml)

[![Python Tweet_relative_account_bot.py](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/Tweet_relative_account_bot_main.yml/badge.svg)](https://github.com/ScottLL/Twitter_search_bot/actions/workflows/Tweet_relative_account_bot_main.yml)


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
![twitter_bots](https://user-images.githubusercontent.com/105904149/207117949-4e53fda5-65a0-483c-87b8-460d34b3ac82.jpeg)

`searching_tweets.py`: searches for tweets every 15 minutes and adds new tweets to a csv file stored in an AWS S3 bucket.

`direct_messages.py`: sends 500 messages per day to English speaking twitter influencers with more than 300 and less than 20,000 followers, using information in the .csv file from AWS S3 bucket.

`tweet_relative_account_bot.py`: retweets content based on popularity every 15 minutes.

`retwitter_content_bot.py`: retweets content based on google searching keywords in google sheet.

`News_df.py` : update the crypto News from CryptoPanic.com.

`News_post.py` : post updates News to twitter.



## Demo Video
[Group Project - Twitter Bots]()


## Sample Output
### Business Development Twitter Bot
#### 1. Build twitter_account_bot() function at Tweet_relative_account_bot.py

<img width="1478" alt="Screen Shot 2022-12-13 at 10 43 23 AM" src="https://user-images.githubusercontent.com/112274822/207389323-3c41aaaa-85b0-4861-a2db-69727e121a84.png">
<img width="1428" alt="Screen Shot 2022-12-13 at 10 44 27 AM" src="https://user-images.githubusercontent.com/112274822/207389372-d93c45f5-e1af-404f-baaf-16c8486eb428.png">

* Goal: Let all official accounts of MEXC automatically post transaction information, knowledge and news related to crypt currency on Twitter. The built-in function automatic update time of this bot is once every 5 minutes.

<img width="585" alt="Screen Shot 2022-12-13 at 11 01 39 AM" src="https://user-images.githubusercontent.com/112274822/207389497-57113ff3-694e-4f30-8ae0-ea26294b20ae.png">

* Main target official accounts: "MEXC_Global", "MEXC_Eilla", "MEXC_VIP", "MEXCDerivatives", "EtfMexc", "MEXC_SEA", "MEXC_Fans", and "MEXC_CEO".

<img width="557" alt="Screen Shot 2022-12-13 at 11 01 48 AM" src="https://user-images.githubusercontent.com/112274822/207389592-36a98d88-2956-4ce4-9eb6-5d9fcb69472b.png">

* Some examples of the results after running twitter_account_bot():

<img width="394" alt="Screen Shot 2022-12-13 at 10 48 12 AM" src="https://user-images.githubusercontent.com/112274822/207389651-a18a4c64-3f4f-40b9-b406-ace8d93a7e0b.png">
<img width="410" alt="Screen Shot 2022-12-13 at 10 46 05 AM" src="https://user-images.githubusercontent.com/112274822/207389656-9b6fa631-ef56-4d06-a9c0-b52f50407e78.png">
<img width="391" alt="Screen Shot 2022-12-13 at 10 47 17 AM" src="https://user-images.githubusercontent.com/112274822/207389662-abdbfa18-31bf-44ad-a4c6-03bb0f49a8bc.png">

#### 2. Test Tweet_relative_account_bot.py functions

* Go to the homepage of the repository, click the button "Actions", and choose "set up a workflow yourself".

<img width="674" alt="Screen Shot 2022-12-13 at 11 21 29 AM" src="https://user-images.githubusercontent.com/112274822/207389775-23c1598a-70bb-4976-9514-50af186c71e8.png">

* Name it as "Tweet_relative_account_bot_main.yml", type the code you need, then click the green button "start commit".

<img width="519" alt="Screen Shot 2022-12-13 at 10 50 23 AM" src="https://user-images.githubusercontent.com/112274822/207389894-85da0901-ab52-4ec8-8c84-c257c69efaeb.png">

*  Once complete these steps, you can check the status of your workflows from "Actions" page, so make sure your program could pass the tests. Otherwise, you need to fix the code where the bugs/errors are reported.
*  Eg. Check out the code for issues:

<img width="1125" alt="Screen Shot 2022-12-13 at 11 25 00 AM" src="https://user-images.githubusercontent.com/112274822/207389737-e1313267-474e-423c-b3f3-22aa9fec5a80.png">
