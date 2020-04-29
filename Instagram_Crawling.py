#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver as wd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 
import re 
keyword = "도심속바다축제" 
url = "https://www.instagram.com/explore/tags/{}/".format(keyword) 
instagram_tags = [] 
instagram_tag_dates = [] 
driver = wd.Chrome("C:/Users/jang/Desktop/chromedriver") 
driver.get(url) 
time.sleep(3) 
driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click() 
for i in range(219): 
    time.sleep(1) 
    try: 
        data = driver.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj 
        tag_raw = data.text 
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw) 
        tag = ''.join(tags).replace("#"," ") # "#" 제거 
        
        tag_data = tag.split() 
        
        for tag_one in tag_data: 
            instagram_tags.append(tag_one) 
            print(instagram_tags) 
            
        date = driver.find_element_by_css_selector("time._1o9PC.Nzb55" ).text # 날짜 선택 
        
        if date.find('시간') != -1 or date.find('일') != -1 or date.find('분') != -1: 
            instagram_tag_dates.append(date) 
        else: 
            instagram_tag_dates.append(date) 
        print(instagram_tag_dates)
        
    except: 
        instagram_tags.append("error") 
        instagram_tag_dates.append('error') 
    try: 
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a._65Bje.coreSpriteRightPaginationArrow'))) 
        driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click() 
    except: 
        driver.close() 
    #date = datum2.text 
    print(date) 
    
    time.sleep(3) 
driver.close()


# In[2]:


print(instagram_tag_dates)


# In[4]:


print(instagram_tags)


# In[2]:


import pandas as pd
insta_tag = pd.DataFrame(instagram_tag_dates,instagram_tags)
print(insta_tag)


# In[ ]:


len(instagram_tag_dates)
len(instagram_tags)


# In[3]:


import pandas as pd
insta_dates_df = pd.DataFrame(instagram_tag_dates)
print(insta_dates_df)


# In[13]:


import collections
from collections import Counter
dates_count = collections.Counter(instagram_tag_dates)
type(dates_count)


# In[14]:


dates_count_df = pd.DataFrame.from_dict(dates_count, orient='index')


# In[10]:


#dates_count_df.to_csv("dates_count_df.csv", header=True, index=True, encoding='cp949')


# In[15]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('C:/Users/jang/Desktop/dates_count_df_rename.csv', encoding='euc-kr')
plt.title('Count per Day')
plt.xlabel('Date')
plt.ylabel('Count')
plt.bar(df['date'], df['count'])
plt.show()


# In[75]:


df = df.sort_values(by = 'count', ascending=False)
#df.head()
len(df)


# In[17]:


df2 = df[0:10]
plt.title('Count per Day')
plt.xlabel('Date')
plt.ylabel('Count')
plt.bar(df2['date'], df2['count'])
plt.show()


# In[18]:


import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
font_location = './malgun.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)


# In[19]:


plt.title('Count per Day')
plt.xlabel('Date')
plt.xticks(rotation = -45)
plt.ylabel('Count')
plt.bar(df2['date'], df2['count'])
plt.show()


# In[5]:


insta_dates_df.columns = ['date']
insta_dates_df.head()


# In[6]:


insta_dates_df['year'] = insta_dates_df['date'].str[0:4]
insta_dates_df.head()


# In[7]:


len(insta_dates_df)


# In[8]:


#insta_dates_df = insta_dates_df.drop(['count'], axis=1)
insta_dates_df = insta_dates_df.drop_duplicates()
len(insta_dates_df)


# In[20]:


#dates_count_df.head()
len(dates_count_df)


# In[15]:


dates_count_df.columns = ['count']
dates_count_df.head()


# In[25]:


insta_dates_df = insta_dates_df.drop(147,0)
len(insta_dates_df)


# In[30]:


#dates_count_df = dates_count_df.drop('error',0)
len(dates_count_df)


# In[31]:


insta_dates_df


# In[32]:


dates_count_df


# In[36]:


dates_count_df = dates_count_df.drop(['year'],1)
dates_count_df


# In[1]:


import matplotlib.pyplot as plt
plt.title('연도별 인스타그램 해시태그 수')
plt.xlabel('year')
plt.xticks(rotation = -45)
plt.ylabel('Count')
plt.bar(insta_dates_df['year'], dates_count_df['count'], align='edge')
plt.show()

