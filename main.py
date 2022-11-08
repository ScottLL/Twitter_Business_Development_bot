from searching_tweets import searchTweets
import time


#       coins = ['BTC','ETH','DOGE','ADA','BNB','XRP','SOL','MATIC','DOT','STETH','SHIB','TRX','DAI','UNI','WBTC','LTC','LEO','OKB','ATOM','LINK','FTT','XLM','CRO','XMR','ALGO','NEAR','TON']
# coins = ['BTC','ETH','DOGE','ADA','DAI','UNI','WBTC','LTC','LEO'] 
coins = ['BTC','ETH']
for i in coins:
    searchTweets(i, int(200/len(coins)))
    time.sleep(60*15)
