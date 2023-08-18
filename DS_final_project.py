#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


# In[3]:


chronic_illness = pd.read_csv("C:/Users/PC/Desktop/chronic illness.csv")
chronic_illness.head()


# first step is to decide which columns I'm going to use and to filter out missing values. I don't need the user_id column, and there are a few missing values. 

# In[5]:


chronic_illness1 = chronic_illness.dropna()


# In[6]:


chronic_illness1.drop(['user_id'], axis=1, inplace=True)


# In[7]:


chronic_illness1.head()


# ## Exploring dataset
# these next steps are going to be used to see what this dataset has to offer.
# Can the data lead to a conclusion about the effectiveness of a patient's symptoms leading to an accurate diagnosis?

# In[8]:


chronic_illness1.info()


# In[10]:


chronic_illness1['trackable_type'].value_counts()


# In[11]:


chronic_illness1['trackable_name'].value_counts()


# In[12]:


chronic_illness1['trackable_id'].value_counts()


# there are almost a million entries and many conditions in this dataset. I'm going to narrow it down. 
# I'm also not sure how to make a connection between the symmptoms and the connection because both are in the same coloumn. Another question may be analyzed. i have back ups. I'm going to drop a few rows.

# In[13]:


chronic_illness2 = chronic_illness1[ : 1000]


# In[14]:


chronic_illness2.head()


# In[15]:


chronic_illness2.info()


# In[16]:


chronic_illness2['trackable_type'].value_counts()


# In[17]:


chronic_illness2['trackable_name'].value_counts()


# I'm altering my thinking a little. I want to figure out the prevelance of anxiety and depression by yet to be determined demographics (age, gender, and/or location). I feel like the outlook on mental health has changed a lot since I was a child. More people ae willing to seek treatment as the stigma around mental health is lessened.

# this is a spot I may need to go back before going forward.

# In[ ]:




