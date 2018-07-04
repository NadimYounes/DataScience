import requests
from bs4 import BeautifulSoup


# In[28]:


url = 'http://www.espnfc.us/fifa-world-cup/4/statistics/scorers'


# In[29]:


page = requests.get(url)


# In[34]:


print(page)
print(page.content)


# In[35]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[36]:


soup.prettify().encode('UTF-8')


# In[101]:


#You can specify a dictionary to filter more specifically using find_all('ul', {class: top-player-stats})
#Since our len(tbody_list) only returns one value we don't need to specify the dictionary
tbody_list = soup.find_all('tbody')
tbody_list


# In[102]:


#Here we use len(tbody_list) to check how many tbody items are being returned, and we get 1 which contains all the top scorers stats!
len(tbody_list)


# In[103]:


# I want to narrow this down more to include the names of players who scored in the world cup
# Please not that we used tbody_list[0] instead of only tbody_list find_all because find_all gives you a list of results rather than just the first result
player_name = tbody_list[0].find_all('a')
player_name


# In[105]:


# We now want to extract the text from this function to clean up all the messy html tags in the list
for i in player_name:
    print(i.text.encode('UTF-8'))
