#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install GetOldTweets3')


# In[2]:


import GetOldTweets3 as got


# In[3]:


from bs4 import BeautifulSoup as bf


# In[4]:


import datetime

days_range = []

start = datetime.datetime.strptime('2019-01-01', '%Y-%m-%d')
end = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')

date_generated = [start + datetime.timedelta(days=x) for x
                  in range(0, (end-start).days)]

for date in date_generated:
  days_range.append(date.strftime('%Y-%m-%d'))

print('=== 설정된 트윗 수집 기간은 {}에서 {} 까지입니다.'.format(days_range[0], days_range[-1]))
print('=== 총 {}일 간의 데이터'.format(len(days_range)))


# In[ ]:


import time

# 수집 기간 맞추기
start_date = days_range[0]
end_date = (datetime.datetime.strptime(days_range[-1], "%Y-%m-%d") 
            + datetime.timedelta(days=1)).strftime("%Y-%m-%d") # setUntil이 끝을 포함하지 않으므로, day + 1

# 트윗 수집 기준 정의
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('힐링')                                           .setSince(start_date)                                           .setUntil(end_date)                                           .setMaxTweets(-1)

# 수집 with GetOldTweet3
print("Collecting data start.. from {} to {}".format(days_range[0], days_range[-1]))
start_time = time.time()

tweet = got.manager.TweetManager.getTweets(tweetCriteria)

print("Collecting data end.. {0:0.2f} Minutes".format((time.time() - start_time)/60))
print("=== Total num of tweets is {} ===".format(len(tweet)))


# In[ ]:


# 원하는 변수 골라서 저장
from random import uniform
from tqdm import tqdm_notebook

tweet_list = []

for index in tqdm_notebook(tweet):
  # 메타데이터 목록
  username = index.username
  #link = index.permalink
  content = index.text
  tweet_date = index.date.strftime("%Y-%m-%d")
  #tweet_time = index.date.strftime("%H:%M:%S")
  #retweets = index.retweets
  #favorites = index.favorites

  # 결과 합치기
  # info_list = [tweet_date, tweet_time, username, content, link, retweets, favorites]
  info_list = [username, tweet_date, content]
  tweet_list.append(info_list)

  time.sleep(uniform(1,2))


# In[ ]:


import pandas as pd
#twitter_df = pd.DataFrame(tweet_list,
#                          columns=['date','time','username','text','link','retweet_counts','facorite_counts'])
twitter_df = pd.DataFrame(tweet_list, columns=['date', 'username', ' text'])

# csv 파일 만들기
twitter_df.to_csv('healing_search_twitter.csv',encoding='utf-8-sig')
print('=== {}개의 트위터가 성공적으로 저장되었습니다.==='.format(len(tweet_list)))


# In[ ]:


rrdf_tweet = pd.read_csv('/content/healing_twitter.csv')
df_tweet.head(10)


# In[ ]:


def get_keywords(dataframe):
  keywords = []
  text = dataframe['text'].lower()
  if '기생충' in text:
    keywords.append("기생충")
  if '후기' in text:
    keywords.append('후기')
  return ','.join(keywords)

df_tweet['keyword'] = df_tweet.apply(get_keywords, axis=1)

import matplotlib.pyplot as plt

counts = df_tweet['keyword'].value_counts()
plt.bar(range(len(counts)),counts)
plt.title("키워드 빈도")
plt.ylabel('트윗 수')
plt.show()
print(counts)

