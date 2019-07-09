#!/usr/bin/env python
# coding: utf-8

# In[108]:


import os
import sqlite3
import csv
import pandas as pd
import numpy as np
import seaborn as sns


# In[109]:


# Create database file called auto_data.db
conn = sqlite3.connect('auto_data.db')


# In[110]:


#auto_data = 0


# In[112]:


# Read the data into a panda dataframe
auto_data = pd.read_csv('car_noise_data.csv')


# In[102]:


print (auto_data)


# In[103]:


auto_data.to_sql('auto_data', conn, if_exists='replace')


# In[64]:


ad = pd.read_sql("SELECT * FROM auto_data", conn)


# In[55]:


ad


# In[ ]:




