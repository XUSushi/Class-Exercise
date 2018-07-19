
# coding: utf-8

# In[1]:

a=[11,2,3,4,66,7,9,111]


# In[2]:

a


# In[3]:

a[3]


# In[4]:

a.pop(8)


# In[5]:

a.pop(7)


# In[6]:

a


# In[7]:

a.insert(22)


# In[8]:

a.insert(7,22)


# In[9]:

a


# In[10]:

a.sort()


# In[11]:

a


# In[30]:

a.sort(reserve = False)


# In[13]:

b=[22,1,2,3,7,4,99]


# In[15]:

c=tuple(b)


# In[16]:

c


# In[20]:

dict1={'he':22,'she':19}


# In[21]:

dict1


# In[23]:

dict1.keys()


# In[24]:

'he' in dict1.keys()


# In[25]:

'me' in dict1.keys()


# In[26]:

dict1['she']


# In[27]:

a


# In[28]:

22 in a


# In[29]:

19 in dict1.values()


# In[31]:

dict1.items()


# In[35]:

for it in dict1.items():print(it[0],it[1])


# In[33]:

x=1


# In[36]:

if x>1:print(x)


# In[37]:

if x<3:print(x)


# In[38]:

if x>1:
    print('x is larger than 1!')
else:
    print('x is smaller than 1!')


# In[39]:

a=15


# In[43]:

xv=15


# In[42]:

if x<15:
    y=10
elif x>15 and x<18:
    y=12
else:
    y=18


# In[44]:

x=16


# In[45]:

y


# In[46]:

def fun1(x):
    if x<15:
        y=10
    elif x>15 and x<18:
        y=12
    else:
        y=18
    return(y)


# In[47]:

fun1(16)


# In[48]:

a=15


# In[49]:

if not a>0:print('yes')


# In[50]:

if not a<0:print('yes')


# In[ ]:



