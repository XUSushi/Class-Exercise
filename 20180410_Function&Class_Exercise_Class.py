
# coding: utf-8

# In[20]:

class animal():
    def __init__(self,name,kind):
        self.name=name
        self.kind=kind
    def getName(self):
        '''a method for getting name'''
        return self.name
    def getKind(self):
        return self.kind
    def changeName(self,newname):
        self.name=newname
        


# In[2]:

A=animal("cat","cat_kind")


# In[3]:

dir(A)


# In[4]:

A.__class__


# In[5]:

A.kind


# In[6]:

A.name


# In[7]:

A.name


# In[8]:

A.changeName(A,"little catty")


# In[9]:

A.changeName(A "little catty")


# In[11]:

A.changeName(A,'catty')


# In[12]:

A.changeName('catty') #改名了！但注意，他的self,是自动的，不用自己再输入了


# In[13]:

a.name


# In[14]:

A.name


# In[15]:

A.getName.__doc__


# In[17]:

help(A.getName.__doc__)


# In[22]:

A.getName.__doc__


# In[23]:

A.getName.__doc__


# In[24]:

print(A)


# In[28]:

class animal():
    def __init__(self,name,kind):
        self.name=name
        self.kind=kind
    def getName(self):
        '''a method for getting name'''
        return self.name
    def getKind(self):
        return self.kind
    def changeName(self,newname):
        self.name=newname
    def __str__(self):
        return(self.name+'---'+self.kind)


# In[29]:

A=animal("cat","cat_kind")


# In[30]:

print(A)


# In[31]:

A.getName.__doc__#得在上面定义函数时写''''''才有doc


# In[33]:

A.__name__


# In[34]:

#定义时_小横线在前面时是私有方法


# In[35]:

class cat(animal):
    def__init__():
        pass


# In[36]:

class cat_asia (cat):
    def__init__():
        pass


# In[37]:

#数组的索引和分片


# In[38]:

a = array([[ 0, 1, 2, 3, 4, 5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])


# In[39]:

from numpy import *


# In[40]:

a = array([[ 0, 1, 2, 3, 4, 5],
           [10,11,12,13,14,15],
           [20,21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51,52,53,54,55]])


# In[41]:

a[0, 3:5]#想得到第一行（0）的第 4 和第 5 （3：5）两个元素：


# In[42]:

a[2,3:6]


# In[43]:

#得到最后两行的最后两列：


# In[44]:

a[4:,4:]


# In[45]:

a[0]


# In[46]:

a[2,1]


# In[47]:

a[:,0]#取第一列，即取所有行第一个


# In[48]:

a[0,:]#第一行


# In[49]:

a[3,2:4]


# In[50]:

a[::2,::2] #隔两行取


# In[51]:

a[(3,5),::]#取第4，6行的所有


# In[52]:

a[(3,5),::2]


# In[53]:

a.max()


# In[54]:

a.sum()


# In[55]:

a.averange()


# In[56]:

a.mean()#平均值


# In[57]:

a.std()#标准差


# In[58]:

a.var()#方差


# In[59]:

a.any()#如果有不为0就是true


# In[60]:

np.zeros(15,15,dtype=int)


# In[65]:

help(np)


# In[64]:

import numpy as np


# In[70]:

a=np.zeros((15,15),dtype=float)


# In[71]:

a


# In[72]:

a.any()


# In[73]:

a[0,0]=1


# In[74]:

a.any()


# In[75]:

a[:,0].any()


# In[76]:

a=range(1,10)


# In[77]:

a


# In[79]:

np.arange(1,10)#快速生成数组


# In[80]:

b=zeros((5,5))#快速生产全为0的数组


# In[81]:

b


# In[82]:

b=np.linspace(0,100,5) #1,100五等分这个数组


# In[83]:

b


# In[ ]:



