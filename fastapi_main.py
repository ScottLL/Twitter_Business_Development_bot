from searching_tweets import searchTweets
from fastapi import FastAPI
import uvicorn
from direct_messages import direct_messages
from newsApp.News_post import news_post
from newsApp.News_df import news_df
from Tweet_relative_account_bot  import twitter_account_bot

app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""
    return {"message": "Hello! This is the home page for querying the cryptocurrency data."}

@app.post("/search_Tweets")
async def search_Tweets(coins:str, max_results:int):
    if max_results <= 250:
        searchTweets(coins, int(max_results/len(coins)))
        return {"message": "Done"}
    else:
        return {"message": "Max Results is too high, try to lower the max results"}

@app.post("/Twitter_Message")
async def Twitter_message(message):
    direct_messages(message)
    return {"message": "Message Send"}


@app.post("/News_data_update")
async def Update_crypto_news():
    news_df()
    return {"message": "News Updated"}

@app.post("/News_Post")
async def post_crypto_news():
    news_post()
    return {"message": "News Posted"}

@app.post("/Twitter_Account_repost")
async def repost_twitter_account():
    twitter_account_bot()
    return {"message": "Account Reposted"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)