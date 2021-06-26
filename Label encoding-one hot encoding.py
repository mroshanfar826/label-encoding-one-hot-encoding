#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder


# In[2]:


airbnb = pd.read_csv('data/Newyourk_airbnb/AB_NYC_2019.csv')


# In[ ]:


airbnb.describe()


# In[ ]:


airbnb.head()


# In[ ]:


airbnb['neighbourhood_group'(اسم ستونی که میخوایم انکد انجام بدیم)].unique()


# In[ ]:


#LabelEncoder
lbl_encode = LabelEncoder()


# In[ ]:


lbl_encode.fit_transform(airbnb['neighbourhood_group'(اسم ستونی که میخوایم انکد انجام بدیم)])


# In[ ]:


airbnb['neighbourhood_group_label']=lbl_encode.fit_transform(airbnb['neighbourhood_group'(اسم ستونی که میخوایم انکد انجام بدیم)])


# In[ ]:


airbnb['neighbourhood_group_label'].value_counts()


# In[ ]:


airbnb['neighbourhood_group'].value_counts()


# In[ ]:


#one-hot encoding
add_columns = pd.get_dummies(airbnb['neighbourhood_group'])


# In[ ]:


add_columns


# In[ ]:


airbnb.join(add_columns)


# In[ ]:


airbnb.drop(['neighbourhood_group'], axis = 1, inplace=True)


# In[ ]:


airbnb.columns


# In[ ]:


airbnb = airbnb.join(add_columns)


# In[ ]:


airbnb


# In[ ]:




