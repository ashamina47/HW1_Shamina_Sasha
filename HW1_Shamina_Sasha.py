#!/usr/bin/env python
# coding: utf-8

# In[ ]:


c = list(range(30, 65, 5))


# In[5]:


print(c)


# In[6]:


print(c[::-1])


# In[7]:


d = c[::-1]


# In[8]:


print(d)


# In[9]:


d.insert(0, 65)


# In[10]:


print(d)


# In[ ]:





# In[11]:


list1 = []


# In[12]:


for item in range(0, 21):
    list1.append(item)


# In[13]:


list1


# In[14]:


del list1[0]


# In[15]:


list1


# In[16]:


print(len(list1))


# In[17]:


print(max(list1))


# In[18]:


print(min(list1))


# In[20]:


print(sum(list1))


# In[ ]:





# In[ ]:





# In[21]:


weather = {'Sunny': 'play', 'Rainy': 'watch TV', 
                  'Cloudy': 'walk'}


# In[22]:


weather


# In[27]:


wetaher = {'Sunny': 'play',
          'Rainy': 'watch TV',
          'Cloudy': 'walk'}


# In[28]:


weather


# In[29]:


for key, value in weather.items():
    print(key, ' : ', value)


# In[37]:


for key, value in weather.items():
    print('When' + ' '+ key +' ' + 'let us' + ' ' + value)


# In[39]:


weather['Snowy'] = 'ski'


# In[40]:


for key, value in weather.items():
    print(key, ' : ', value)


# In[ ]:




