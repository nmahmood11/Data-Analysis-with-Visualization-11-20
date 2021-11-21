#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import Panda libraries
import pandas as pd


# In[18]:


# Import datasets 
movies = pd.read_csv(r'C:\Users\Noman Mahmood\Desktop\DS\movie2.csv', sep=',')


# In[19]:


print(type(movies))
movies.head(20)


# In[5]:


tags = pd.read_csv(r'C:\Users\Noman Mahmood\Desktop\DS\tag3.csv', sep=',')
tags.head()


# In[17]:


ratings = pd.read_csv(r'C:\Users\Noman Mahmood\Desktop\DS\rating2.csv', sep=',', parse_dates=['timestamp'])
ratings.head()


# In[20]:


del ratings['timestamp']
del tags['timestamp']


# In[21]:


row_0 = tags.iloc[0]
type(row_0)


# In[22]:


print(row_0)


# In[23]:


row_0.index


# In[24]:


row_0['userId']


# In[26]:


'rating' in row_0


# In[27]:


row_0.name


# In[28]:


row_0 = row_0.rename('firstRow')
row_0.name


# In[29]:


tags.head()


# In[30]:


tags.index


# In[31]:


tags.columns


# In[32]:


tags.iloc[ [0,11,500] ]


# In[33]:


#statistics 
ratings['rating'].describe()


# In[35]:


ratings.describe()


# In[36]:


ratings['rating'].mean()


# In[37]:


ratings.mean()


# In[38]:


ratings['rating'].min()


# In[39]:


ratings['rating'].max()


# In[40]:


ratings['rating'].std()


# In[41]:


ratings['rating'].mode()


# In[42]:


ratings.corr()


# In[43]:


#Apply Filters
filter1 = ratings['rating'] > 10
print(filter1)
filter1.any()


# In[45]:


filter2 = ratings['rating'] > 0
filter2.all()


# In[46]:


#data Claening ( Missing data)
movies.shape


# In[47]:


movies.isnull().any().any()
# Yay no Null Values 


# In[48]:


ratings.shape


# In[49]:


ratings.isnull().any().any()
# Yay no null values


# In[50]:


tags.shape


# In[51]:


tags.isnull().any().any()
#ops found null values


# In[52]:


tags=tags.dropna()
# remove null values


# In[53]:


tags.isnull().any().any()


# In[54]:


# Data Viaualization 
get_ipython().run_line_magic('matplotlib', 'inline')

ratings.hist(column='rating', figsize=(10,5))


# In[55]:


ratings.boxplot(column='rating', figsize=(10,5))


# In[56]:


# Slicing (columns)
tags['tag'].head()


# In[57]:


movies[['title','genres']].head()


# In[58]:


ratings[-10:]


# In[59]:


tag_counts = tags['tag'].value_counts()
tag_counts[-10:]


# In[60]:


tag_counts[:10].plot(kind='bar', figsize=(10,5))


# In[61]:


#filter selected rows
is_highly_rated = ratings['rating'] >= 5.0
ratings[is_highly_rated][30:50]


# In[62]:


is_action= movies['genres'].str.contains('Action')
movies[is_action][5:15]


# In[63]:


movies[is_action].head(15)


# In[64]:


ratings_count = ratings[['movieId','rating']].groupby('rating').count()
ratings_count


# In[65]:


average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()


# In[66]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.head()


# In[67]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.tail()


# In[68]:


#Merge Data Frames
tags.head()


# In[69]:


movies.head()


# In[70]:


t = movies.merge(tags, on='movieId', how='inner')
t.head()


# In[71]:


#geeper data analysis
avg_ratings= ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']
avg_ratings.head()


# In[72]:


box_office = movies.merge(avg_ratings, on='movieId', how='inner')
box_office.tail()


# In[73]:


is_highly_rated = box_office['rating'] >= 4.0
box_office[is_highly_rated][-5:]


# In[74]:


is_Adventure = box_office['genres'].str.contains('Adventure')
box_office[is_Adventure][:5]


# In[75]:


box_office[is_Adventure & is_highly_rated][-5:]


# In[76]:


#vectorize string operation
movies.head()


# In[79]:


#slipt into multiple columns
movie_genres = movies['genres'].str.split('|', expand=True)


# In[78]:


movie_genres[:10]


# In[80]:


# add a flag
movie_genres['isComedy'] = movies['genres'].str.contains('Comedy')


# In[81]:


movie_genres[:10]


# In[82]:


#extract year
movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)


# In[83]:


movies.tail()


# In[85]:


#prasing time stamp
tags = pd.read_csv(r'C:\Users\Noman Mahmood\Desktop\DS\tag3.csv', sep=',')


# In[95]:


tags.dtypes


# In[96]:


tags.head(5)


# In[94]:


tags['parsed_time'] = pd.to_datetime(tags['timestamp'], unit='s')


# In[89]:


tags['parsed_time'].dtype


# In[90]:


tags.head(2)


# In[97]:


greater_than_t = tags['parsed_time'] > '2015-02-01'

selected_rows = tags[greater_than_t]

tags.shape, selected_rows.shape


# In[98]:


tags.sort_values(by='parsed_time', ascending=True)[:10]


# In[99]:


average_rating = ratings[['movieId','rating']].groupby('movieId', as_index=False).mean()
average_rating.tail()


# In[100]:


joined = movies.merge(average_rating, on='movieId', how='inner')
joined.head()
joined.corr()


# In[ ]:




