"""
CryptoPanic API Formatter.
Use Wrapper to make calls and get data.
Format data for streaming input and monitoring.
Historical Data seems to be limited to 12/24/2018 but there is no Documentation.
"""
import news_api_gather as news_api_gather
import pandas as pd
from datetime import datetime
import os


access_key = os.environ["AWS_ACCESS_KEY_ID"]
secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]

url_everything = news_api_gather.make_url(filter='hot')
everything_pages_last_100 = news_api_gather.get_pages_list_json(9, url_everything)

everything_pages_last_100_results = []
for page in everything_pages_last_100:
    everything_pages_last_100_results.append(page['results'])
df_results = news_api_gather.concatenate_pages(everything_pages_last_100_results)

df_results = pd.DataFrame(df_results)
df_results = df_results[['votes','title', "url",'created_at',"id"]]
df_results['important'] = df_results['votes'].apply(lambda x: x.get('important'))
df_results['positive'] = df_results['votes'].apply(lambda x: x.get('positive'))
df_results['negative'] = df_results['votes'].apply(lambda x: x.get('negative'))
df_results_important = df_results.loc[(df_results['important'] >= 10) & (df_results['positive'] > df_results['negative'])]

df_results_important.to_csv(
    "s3://projecttwitterbot/emotion/news_emotion.csv",
    storage_options={"key": access_key, "secret": secret_access_key})

