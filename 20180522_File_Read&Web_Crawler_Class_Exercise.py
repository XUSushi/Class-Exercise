
# coding: utf-8

# In[2]:

from docx import Document


# In[3]:

from docx import Document


# In[4]:

import docx
from docx import Document


# In[6]:

path = "C:\\Users\\许某某\\Desktop\\word.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)


# In[7]:

html=pq(url="http://www.ftchinese.com/story/001077690")


# In[8]:

from pyquery import PyQuery as pq


# In[9]:

html=pq("http://www.ftchinese.com/story/001077690")


# In[10]:

html.text()


# In[12]:

html.html()


# In[13]:

html('.story-lead').text()


# In[14]:

html('.story-body').text()


# In[15]:

from pyquery import PyQuery as pq


# In[ ]:



