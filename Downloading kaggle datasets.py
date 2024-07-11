#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install kaggle')


# In[4]:


get_ipython().system('mkdir ~/.kaggle')


# In[6]:


get_ipython().system('cp /Users/gangasingh/Downloads/kaggle.json /Users/gangasingh/.kaggle')


# In[11]:


get_ipython().system('cd /Users/gangasingh/.kaggle && ls')


# In[13]:


get_ipython().system("kaggle datasets list -s 'covid'")


# In[16]:


get_ipython().system('kaggle datasets download --force imdevskp/corona-virus-report')


# In[20]:


get_ipython().system('sudo apt-get install unzip')


# In[27]:


get_ipython().system('unzip corona-virus-report.zip')


# In[24]:


get_ipython().system('mkdir data')


# In[29]:


get_ipython().system('mv *.csv data')


# In[ ]:




