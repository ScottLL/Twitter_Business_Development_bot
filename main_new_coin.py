from searching_tweets import searchTweets


#     coins = ['BTC','ETH','DOGE','ADA','BNB','XRP','SOL','MATIC','DOT','STETH','SHIB','TRX','DAI','UNI','WBTC','LTC','LEO','OKB','ATOM','LINK','FTT','XLM','CRO','XMR','ALGO','NEAR','TON']
coins = ["XLM", "CRO", "XMR", "OKB", "ATOM", "LINK", "BNB", "MEXC"]
#     coins = ['BTC','ETH']
for i in coins:
    searchTweets(i, int(250 / len(coins)))
    # print(new_df.tail())
print("Done")