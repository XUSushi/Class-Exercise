
# coding: utf-8

# In[1]:

from numpy import pi


# In[2]:

from math import rand


# In[3]:

help(read)


# In[4]:

import random


# In[5]:

x=rand(200)


# In[6]:

x=random.random(200)


# In[7]:

x=array([i for i in range(1,50)])


# In[8]:

from numpy import *


# In[9]:

get_ipython().magic('pylab')


# In[10]:

a = [1, 2, 3, 4]


# In[11]:

a = array(a)


# In[12]:

a


# In[13]:

a+1


# In[15]:

b=array([2,3,4,5])


# In[16]:

a+b


# In[17]:

a*b


# In[18]:

a**b


# In[19]:

a = linspace(0, 2*pi, 21)
get_ipython().magic('precision 3')


# In[20]:

a


# In[21]:

b=sin(a)


# In[22]:

b


# In[23]:

get_ipython().magic('matplotlib inline')
plot(a, b)


# In[24]:

b>=0


# In[25]:

mask=b>=0


# In[26]:

plot(a[mask], b[mask], 'ro')


# In[27]:

from numpy import pi


# In[28]:

from numpy import array, sin


# In[29]:

a = [i for i in range(1,20)]


# In[30]:

a


# In[31]:

#可以这样创建


# In[32]:

a = array([[1,2,3],[1,2,3],[1,2,3]])


# In[33]:

a


# In[34]:

a.shape  


# In[35]:

a[1,1]


# In[36]:

a = array([[ 0, 1, 2, 3, 4, 5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])


# In[37]:

a


# In[39]:

a[2:4,:52]


# In[40]:

label='verb','noun','adj','prep'


# In[42]:

size=[30,30,25,15]


# In[43]:

color=['red','green','blue','yellow']


# In[44]:

import matplotlib.pyplot as plt


# In[45]:

explode = (0, 0.1, 0, 0)


# In[116]:

plt.pie(size,explode=explode,labels=label,colors=color,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()


# In[54]:

plt.axis('equal')


# In[55]:

plt.show()


# In[61]:

from nltk import *
from nltk.corpus import PlaintextCorpusReader as PCR


# In[64]:

files=PCR("D:\corpara",".*\.txt")


# In[68]:

files.fileids()


# In[73]:

from nltk import pos_tag


# In[72]:

words = word_tokenize(files.raw(fileids=files.fileids()))


# In[74]:

words


# In[75]:

tagged=pos_tag(words)#查看词形


# In[76]:

tagged


# In[88]:

f=open("D:/chinese_eg.txt",'r',encoding='UTF-8')
c=f.read()
corpus=SnowNLP(c)


# In[78]:

#r 只读


# In[79]:

from snownlp import SnowNLP


# In[89]:

corpus.sentences


# In[90]:

standfordnlp


# In[103]:

corpus.words


# In[106]:

tags=[tag for tag in corpus.tags]  #对词性进行标记


# In[107]:

tags


# In[108]:

corpus.sentiments#情感分析


# In[117]:

plt.pie(size,labels=label,colors=color,
        )
#课上示例


# In[ ]:



