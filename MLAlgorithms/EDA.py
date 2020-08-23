

import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\rahul03\SpyderProjects\DataScience\MLAlgorithms\car.txt')
df.head(5)


# In[115]:


df.shape


# In[24]:


df.isnull().values.any()


# In[32]:


df.isnull().sum().sum()


# In[31]:


df[df.isna().any(axis=1)]


# In[35]:


df = df.dropna()


# In[36]:


df[df.isna().any(axis=1)]


# In[40]:


df.isnull().values.any()


# In[39]:


df.isnull().sum().sum()


# In[44]:


df.shape


# In[55]:


import matplotlib as plt
df.plot(x ='Present_Price', y='Selling_Price', kind = 'scatter')
#plt.show()


# In[72]:


import seaborn as sns
sns.boxplot(y=df['Year'])


# In[89]:


df.min()


# In[100]:


df.nsmallest(5, ['Year']) 


# In[104]:


print(df[df['Year'] < 2005] )


# In[118]:


df = df[df['Year'] > 2005]
sns.boxplot(y=df['Year'])


# In[128]:


df.shape


# In[131]:


from numpy import percentile
quartiles = percentile(df['Year'], [25, 50, 75])
print(df.min()['Year']) 


# In[139]:


print(df.min()['Year']) 
print(quartiles[0])
print(quartiles[1])
print(quartiles[2])
print(df.max()['Year']) 


# In[146]:


print(df['Year'].mean()) 
print(df['Year'].median()) 
print(df['Year'].mode()) 
print(df['Year'].std()) 
print(df['Year'].var()) 


# In[156]:


import matplotlib.pyplot as plt
plt.hist(df['Year'], bins=len(df['Year'].unique()))
plt.gca().set(title='Frequency Histogram', ylabel='Frequency')


# In[161]:


df['Year'].plot(kind='density')
plt.show()

