#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

import plotly.express as px

df=pd.read_csv('30min_N50_10yr[1].csv')
df.head(50)


# In[5]:



figure=px.scatter(df,x="date" , y="close")
figure.show()


# In[6]:


figure=px.line(df,x="date" , y="close",title="Nifty 50 2015-2021 analysis")
figure.update_xaxes(rangeslider_visible=True)

figure.show()


# In[7]:


figure=px.line(df,x="date" , y="close",title="Nifty 50 2015-2021 analysis")
figure.update_xaxes(rangeselector=dict(
    buttons=list([
    dict(count=1,label='1d' ,  step="day", stepmode="backward"),
    dict(count=1,label='1m' ,  step="month", stepmode="backward"),
    dict(count=6,label='6m' ,  step="month", stepmode="backward"),
    dict(count=3,label='3m' ,  step="month", stepmode="backward"),
    dict(count=1,label='1y' ,  step="year", stepmode="backward"),
    dict(step="all")
])))
figure.show()


# In[ ]:





# In[27]:





# In[ ]:




