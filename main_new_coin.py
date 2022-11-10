from searching_tweets import searchTweets



#     coins = ['BTC','ETH','DOGE','ADA','BNB','XRP','SOL','MATIC','DOT','STETH','SHIB','TRX','DAI','UNI','WBTC','LTC','LEO','OKB','ATOM','LINK','FTT','XLM','CRO','XMR','ALGO','NEAR','TON']
#     coins = ['BTC','ETH','DOGE','ADA','DAI','UNI','WBTC','LTC','LEO','FTT','ALGO','NEAR','TON'] 
#     coins = ['BTC','ETH']
coins = ['XLM','CRO','XMR','OKB','ATOM','LINK','BNB','XRP']
for i in coins:
    searchTweets(i, int(250/len(coins)))
