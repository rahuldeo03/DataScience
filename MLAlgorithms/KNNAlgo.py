# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:39:47 2020

@author: Rahul03
"""


#!/usr/bin/env python
# coding: utf-8

# In[153]:


import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\rahul03\SpyderProjects\DataScience\MLAlgorithms\car.txt')
df.head(5)


# In[154]:


#Dropping null rows
df = df.dropna()
df.head(5)


# In[155]:


# dropping usless columns
df = df.drop(['Car_Name'], axis=1)
df1 = df.drop(['Seller_Type'], axis=1)
df1.head(5)


# In[156]:


df2 = pd.get_dummies(df1, prefix='Fuel_Type_', columns=['Fuel_Type'])
df2 = df2.drop(['Fuel_Type__CNG'], axis=1)
df2.head(5)


# In[157]:


df3 = pd.get_dummies(df2, prefix='Transmission_', columns=['Transmission'])
df3 = df3.drop(['Transmission__Automatic'], axis=1)
df3.head(5)


# In[158]:


col_sp = df['Selling_Price']
col_sp.head(5)
df.drop(labels=['Selling_Price'], axis=1,inplace = True)
df.insert(7, 'Sale_Price', col_sp)
df.head(5)


# In[159]:


X = df3.iloc[:, :-1].values
y = df3.iloc[:, 7].values
print(X)


# In[160]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


# In[161]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[162]:


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)


# In[163]:


y_pred = classifier.predict(X_test)


# In[164]:


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# In[165]:


error = []

# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))


# In[167]:


import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

