#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
cars = pd.read_csv('cars.csv')


# In[8]:


print(cars.iloc[:5, ::2])


# In[9]:


print(cars.loc[cars['Model'] == 'Mazda RX4'])


# In[10]:


print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])


# In[11]:


models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(models), ['cyl', 'gear']])


# In[ ]:




