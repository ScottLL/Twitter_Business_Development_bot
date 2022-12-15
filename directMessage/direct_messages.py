import pandas as pd
import tweepy
import os
from smart_open import smart_open  

def direct_messages(message):
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    token = os.environ["TOKEN"]
    token_secret = os.environ["TOKEN_SECRET"]
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
    secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)

   # get the search results
    df = pd.read_csv(smart_open('s3://projecttwitterbot/Searching/search_df.csv'), lineterminator='\n')
    user_id_dataFrame = pd.read_csv(smart_open('s3://projecttwitterbot/Message/user_id.csv'), lineterminator='\n')

    sort_df = df[(df.lang == 'en') & (df.followers_count >= 300)
                 & (df.followers_count <= 20000)]
    sort_df = sort_df.reset_index()
    # print(sort_df.tail(10))
    user_id = []
    for i in range(len(sort_df[-500:-1])):  #len(sort_df)):[300:550]
        try:
            user = (api.get_user(screen_name=sort_df.username[i]).id_str) # get the user id
            # last_dms = user in user_id_dataFrame['user_id'].unique() # check if the user id is already in the user_id.csv
            # if last_dms is False:
            # print(user)
            if user in user_id_dataFrame['user_id'].unique():
                continue 
            else:
                #send direct messages to the user
                api.send_direct_message(user, message)
                user_id.append(user)
                
        except:
            pass
    user_id_df = pd.DataFrame(user_id, columns=["user_id"]) # create a dataframe of user id
    # print(user_id_df)
    user_df = pd.concat([user_id_dataFrame, user_id_df]).drop_duplicates().reset_index(drop= True)   # add the user id to the dataframe
    user_df = pd.DataFrame(user_df['user_id']) # remove the nan values
    # print(user_df)
    # add the user id to the user_id.csv on s3
    user_df.to_csv('s3://projecttwitterbot/Message/user_id.csv',
            storage_options={'key': access_key, 'secret': secret_access_key})


if __name__ == "__main__":
    # direct_messages("Hey, how are you doing? I'm Scott, a business development manager working for MEXC Global exchange. I'm crossing through the tweets and found your page. I like your posts, and you could be a perfect fit for the MEXC affiliate program. So I'm sending my warm invitation for you to join MEXC as an affiliate and earn the commitment share and other bonuses from us. Let's me know if you want to know more. I'd happy to make a short call or zoom meeting with you.")
    direct_messages("Hey, How's your day goes so far?")
    
