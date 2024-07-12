#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


get_ipython().system('pip install pandas')


# In[29]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[5]:


URL='https://www.amazon.com/s?k=playstation+4&crid=3VISAFZVN8TC0&sprefix=playstation+4%2Caps%2C1718&ref=nb_sb_noss_1'


# In[6]:


HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})


# In[7]:


webpage=requests.get(URL,headers=HEADERS)


# In[10]:


type(webpage.content)


# In[11]:


soup=BeautifulSoup(webpage.content,'html.parser')


# In[12]:


soup


# In[13]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


# In[14]:


links


# In[19]:


link=links[0].get('href')


# In[20]:


product_list = "https://amazon.com" + link


# In[21]:


product_list


# In[22]:


new_webpage = requests.get(product_list, headers=HEADERS)


# In[23]:


new_webpage


# In[24]:


new_soup = BeautifulSoup(new_webpage.content, "html.parser")


# In[25]:


new_soup


# In[26]:


new_soup.find("span", attrs={"id":'productTitle'}).text.strip()


# In[27]:


new_soup.find("span", attrs={"class":'a-price a-text-price a-size-medium'}).find("span", attrs={"class": "a-offscreen"}).text


# In[28]:


new_soup.find("span", attrs={"class":'a-icon-alt'}).text


# In[ ]:


# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price

# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""	

    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()
         
    except AttributeError:
        available = "Not Available"	

    return available


# In[ ]:


if __name__ == '__main__':

    # add your user agent 
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL ='https://www.amazon.com/s?k=playstation+4&crid=3VISAFZVN8TC0&sprefix=playstation+4%2Caps%2C1718&ref=nb_sb_noss_1'

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[],"availability":[]}
    
    # Loop for extracting product details from each link 
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review_count(new_soup))
        d['availability'].append(get_availability(new_soup))

    
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)


# In[33]:


amazon_df


# In[ ]:




