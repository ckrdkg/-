#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install konlpy


# In[2]:


from konlpy.tag import Okt
from collections import Counter


# In[3]:


file = open('healing_twitter.csv','r', encoding='utf-8')
lists = file.readlines()
file.close()


# In[4]:


okt = Okt()
morphs = []

for sentence in lists:
  morphs.append(okt.pos(sentence))

print(morphs[0:10])


# In[5]:


noun_list = []

for sentence in morphs:
  for word, tag in sentence:
    if len(word) > 1 and tag in ["Noun"] :
      noun_list.append(word)

print(noun_list)


# In[6]:


count = Counter(noun_list)
words = dict(count.most_common())
words


# In[7]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib
from IPython.display import set_matplotlib_formats
matplotlib.rc('font', family = 'malgun.ttf')

set_matplotlib_formats('retina')

matplotlib.rc('axes', unicode_minus=False)


# In[10]:


import numpy as np
import random
from PIL import Image

mask = np.array(Image.open('mask.png'))
mask2 = np.array(Image.open('mask2.png'))
#mask3 = np.array(Image.open('/content/drive/My Drive/Toy Project/jjang.PNG'))

stopwords = {'게임', '하나', '구룡', '노래', '오늘', '사랑', '그냥', '레트로', "옛날"}
#stopwords = set(stopwords)
#stopwords.add('레트로')


# In[11]:


wordcloud = WordCloud(background_color='white',
                      font_path='malgun.ttf',
                      #colormap = 'Accent_r',
                      width = 1200,
                      height= 800,
                      mask = mask,
                      max_words=60,
                      #stopwords = ['레트로']
                     )

wc = wordcloud.generate_from_frequencies(words)
plt.figure(figsize=(15,15))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis=('off')
plt.show()


# In[ ]:




