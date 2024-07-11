#!/usr/bin/env python
# coding: utf-8

# In[2]:


import boto3
import pandas as pd


# In[4]:


s3 = boto3.resource(
    service_name = 's3',
    region_name = 'reg_name',
    aws_access_key_id = 'your_access_key',
    aws_secret_access_key= 'secret_code'
)


# In[5]:


for bucket in s3.buckets.all():
    print(bucket.name)


# In[6]:


get_ipython().system('pip install s3fs')


# In[8]:


import os
os.environ["AWS_DEFAULT_REGION"] = ''
os.environ["AWS_ACCESS_KEY_ID"] = ''
os.environ["AWS_SECRET_ACCESS_KEY"] = ''


# In[12]:


bucket_name = 'bucket_name'

data_dir = '/Users/gangasingh/data/'

for file_name in os.listdir(data_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(data_dir, file_name)
        s3_key = f'{file_name}.csv'
        try:
            s3.Bucket(bucket_name).upload_file(Filename=file_path, Key=s3_key)
            print(f"{file_name} Uploaded to S3 Bucket")
        except Exception as e:
            print(f"Failed to upload {file_name}: {e}")


# In[ ]:




