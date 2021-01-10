# numpy, pandas, matplotlib practice

# Watch those materials if possible

# numpy tutorial: https://www.w3schools.com/python/numpy_intro.asp

# pandas tutorial: https://www.youtube.com/watch?v=PfVxFV1ZPnk

# funtional programming youtube video: https://www.youtube.com/watch?v=goypZR_lQ7I

# matplotlib tutorial: https://matplotlib.org/tutorials/index.html

# practice:

# 首先熟悉resources 下面是不同的人对于不同电影的评分，分别存储在几个不同的文件里。每个文件头上是各个栏的TITLE。
# 其次通过数据处理，进行数据的合并，生成一个EXCEL表格，将用户评分的如下信息列出来。注意有的客户可能对几个不同的电影打分，并且有可能对同一个电影进行多次评分。
# EXCEL表格内容包括  用户基本信息 （id, 名字，职业，电影名，电影类别，评分，打分日期）
# 通过图标进行一些简单的数据分析，例如，什么从用户角度，什么职业的人最多，用户评分最多是什么，再比如，从电影角度，哪种类型的电影最受欢迎，等等* (try yourself)

import numpy as np
import pandas as pd
import openpyxl
import datetime


ratings = pd.read_csv('resources/customers_rating_movies_data/u.data', sep='\t', header=0)
ratings = ratings.reset_index()
col_header = ['user id', 'item id', 'rating', 'timestamp']
ratings.columns = col_header
ratings = ratings.sort_values(['user id','item id']).reset_index(drop=True)

# Reformatting u.item that includes movie information
movie_info = pd.read_csv('resources/customers_rating_movies_data/u.item', sep='\t', header=0)
movie_info1 = movie_info["movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western |"].str.split("|", expand = True)
movie_header = "movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western".split(" | ")
movie_info1.columns = movie_header

# Reformatting u.user that includes user info
user_info = pd.read_csv('resources/customers_rating_movies_data/u.user', sep='\t', header=0)
user_info1 = user_info["user id | age | gender | occupation | zip code"].str.split("|", expand = True)
user_header = "user id | age | gender | occupation | zip code".split(" | ")
user_info1.columns = user_header

# Start integrating information from the three dataframes

ratings.insert(1, 'occupation', ratings['user id'])
ratings['occupation'] = ratings['occupation'].apply(lambda x: user_info1.loc[x-1, 'occupation'])
ratings.insert(3, 'movie name', ratings['item id'])
ratings['movie name'] = ratings['movie name'].apply(lambda x: movie_info1.loc[x-1, 'movie title'])

# Reformat timestamp into date
ratings['timestamp'] = ratings['timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(x))
ratings['date of rating'] = ratings['timestamp'].dt.date
ratings.drop('timestamp', 1, inplace = True)
print(ratings)

def print_genres(x):
    genres = []
    col_index = 5
    for dummy in movie_info1.iloc[x-1, 5:23]:
        if dummy == '1':
            genres.append(movie_info1.columns[col_index])
        col_index += 1
    g_str = '; '.join(genres)
    return g_str



ratings['movie genres'] = ratings['item id'].apply(lambda x: print_genres(x))

# Generate the excel sheet
ratings.to_excel(r'resources/customers_rating_movies_data/ratings.xlsx')


