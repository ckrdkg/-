#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt


# In[4]:


f = open('healing_space_twitter.csv','r',
         encoding='UTF-8')
lines = f.readlines()
f.close()


# In[5]:


pip install konlpy


# In[6]:


from konlpy.tag import Hannanum
hannanum = Hannanum()


# In[7]:


data = []
for i in range(len(lines)):
  data.append(hannanum.nouns(re.sub('[^가-힣a-zA-Z\s]','',lines[i])))
data[:5]


# In[8]:


pip install apyori


# In[ ]:


# 어프라이어리 Apriori
# Support 두 항목 X, Y의 지지도는 전체 수 중 X, Y를 모두 포함하는 건수의 비율
from apyori import apriori
result = (list(apriori(data, min_support=0.04)))
df = pd.DataFrame(result)
df['length'] = df['items'].apply(lambda x: len(x))
df = df[(df['length'] == 2) &
        (df['support'] >= 0.5)].sort_values(by='support', ascending=False)
df.head()


# In[8]:


# networkx 그래프 정의
G = nx.Graph()
ar = (df['items']); G.add_edges_from(ar)


# In[9]:


# 페이지랭크
pr = nx.pagerank(G)
nsize = np.array([v for v in pr.values()])
nsize = 2000 * (nsize - min(nsize)) / (max(nsize) - min(nsize))


# In[ ]:


import matplotlib.font_manager as fm
import matplotlib
import matplotlib.pyplot as plt

font_path = "malgun.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()

matplotlib.rc('font', family=font_name)


# In[29]:


#pos = nx.fruchterman_reingold_layout(G)
#pos = nx.spring_layout(G)
pos = nx.kamada_kawai_layout(G)


# In[30]:


# 네트워크 그래프
plt.figure(figsize=(16,12))
plt.axis('off')
nx.draw_networkx(G, font_family=font_name, font_size=20,
                 pos=pos, node_color = list(pr.values()), node_size=nsize,
                 alpha=1, edge_color='.6')


# In[ ]:




