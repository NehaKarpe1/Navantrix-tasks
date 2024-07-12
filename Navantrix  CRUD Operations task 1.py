#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 


# In[51]:


#CREATE A DATAFRAME
df=pd.read_excel('cookies sales dataset.xlsx')


# In[34]:


# READING THE DATAFRAME 
df.head()


# In[35]:


df.tail()


# In[36]:


df[(df['Customer ID']==1)&(df['Revenue'] > 8000)]


# In[60]:


df[df['Customer ID']==4]


# In[63]:


#INSERTING NEW RECORDS IN DATAFRAME
def add_record(customer_id, order_id, product, units_sold, revenue, cost):
   
    global df  
    new_record = pd.DataFrame({
        'Customer ID': [customer_id],
        'Order ID': [order_id],
        'Product': [product],
        'Units Sold': [units_sold],
        'Revenue': [revenue],
        'Cost': [cost]
    })
    
    df = pd.concat([df, new_record], ignore_index=True)
    return df
# Adding a new record
df = add_record(4, 104, 'D', 25, 10000, 7000)
print(df)


# In[53]:


print(df.tail())


# In[61]:


df = add_record(10, 105, 'choclate', 25, 10000, 7000)


# In[64]:


df[df['Customer ID']==10]


# In[78]:


#MODIFY EXISTING RECORD 
def modify_records(df, customer_id, order_id, new_units_sold, new_revenue):
     mask = (df['Customer ID'] == customer_id) & (df['Order ID'] == order_id)
     df.loc[mask, 'Units Sold'] = new_units_sold
     df.loc[mask, 'Revenue'] = new_revenue
     return df
modify_records(df, customer_id=4, order_id=104, new_units_sold=15, new_revenue=150)


# In[80]:


df.loc[df['Customer ID']==10,'Product']='chocolate'


# In[81]:


df[df['Customer ID']==10]


# In[83]:


#DELETE THE RECORDS
def delete_records(df, customer_id, order_id):
    mask = (df['Customer ID'] == customer_id) & (df['Order ID'] == order_id)
    df = df[~mask]
    return df
delete_records(df,4,104)


# In[ ]:




