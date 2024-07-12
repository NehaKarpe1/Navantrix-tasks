#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd 

df=pd.read_excel('updated cookies sales.xlsx')
get_ipython().system('pip install pandas plotly dash')


# In[21]:


df.head()


# In[20]:


# Check for missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())


# In[7]:


import plotly.express as px

# Group by Product and sum Units Sold
product_units_sold = df.groupby('Product')['Units Sold'].sum().reset_index()

# Create bar chart
fig1 = px.bar(product_units_sold, x='Product', y='Units Sold', title='Total Units Sold by Product')

# Display the chart
fig1.show()


# In[8]:


# Create scatter plot
fig2 = px.scatter(df, x='Revenue', y='Cost', title='Revenue vs. Cost', hover_data=['Customer ID'])

# Display the chart
fig2.show()


# In[9]:


# Calculate revenue share by product
product_revenue = df.groupby('Product')['Revenue'].sum().reset_index()
product_revenue['Revenue Share'] = product_revenue['Revenue'] / product_revenue['Revenue'].sum()

# Create pie chart
fig3 = px.pie(product_revenue, values='Revenue Share', names='Product', title='Revenue Share by Product')

# Display the chart
fig3.show()


# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# In[16]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Cookies Sales Dashboard'),
    
    dcc.Graph(id='bar-chart', figure=fig1),
    
    dcc.Graph(id='scatter-plot', figure=fig2),
    
    dcc.Graph(id='pie-chart', figure=fig3)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




