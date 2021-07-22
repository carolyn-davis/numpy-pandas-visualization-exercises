#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:22:52 2021

@author: carolyndavis
"""

# =============================================================================
#                         ADVANCED DF EXERCISES PART 1
# =============================================================================
# =============================================================================
# Run python -m pip install pymysql from your terminal to install pymysql.
# 
# 1.)Create a notebook or python script named advanced_dataframes to do your work in 
# for these exercises.
# 
# 2.)Run python -m pip install pymysql from your terminal to install the mysql client 
# (any folder is fine)
# cd into your exercises folder for this module and run echo env.py >> .gitignore
# =============================================================================

# =============================================================================
# 3.)Create a function named get_db_url. It should accept a username, hostname, password,
#  and database name and return a url connection string formatted like in the example 
#  at the start of this lesson
# =============================================================================

import pandas as pd
import numpy as np

from env import host, user, password


def get_db_url(user, host, password, database, query):
    
    url = f'mysql+pymysql://{user}:{password}@{host}/employees'
    
    return pd.read_sql(query, url)





# =============================================================================
# 4.)Use your function to obtain a connection to the employees database.
# =============================================================================

emp_df = get_db_url(user, host, password, 'employees', 'select * from employees')
emp_df.head()


# =============================================================================
# 5.)Once you have successfully run a query:
# =============================================================================

# a. Intentionally make a typo in the database url. What kind of error message do you see?
url = f'mysql+pymysql://{user}:{password}@{host}/employee'
#Ans: "Access denied for user to database 'employee'


# b. Intentionally make an error in your SQL query. What does the error message look like?

pd.read_sql('SELECT * FROM: employees LIMIT 5 OFFSET 50', url)
#Ans: You have an error in your SQL syntax: Check the manual....

# =============================================================================
# 6.)Read the employees and titles tables into two separate DataFrames
# =============================================================================
emp_df = get_db_url(user, host, password, 'employees', 'select * from employees')
emp_df.head()   #gets employees tables from emp db, creates df

title_df = get_db_url(user, host, password, 'employees', 'select * from titles')
title_df.head()  #gets titles tables from emp db, creates df


# =============================================================================
# 7.)How many rows and columns do you have in each DataFrame? Is that what you expected?
# =============================================================================
emp_df.shape
#Ans: 300024 rows, 6 columns

title_df.shape
#Ans: 443308 rows, 4 columns

# =============================================================================
# 8.)Display the summary statistics for each DataFrame.
# =============================================================================
emp_df.info()
emp_df.describe()       #Summary for employees df

title_df.info()
title_df.describe()     #Summary for titles df


# =============================================================================
# 9.)How many unique titles are in the titles DataFrame?
# =============================================================================
title_df['title'].unique()
#Ans: 7

# =============================================================================
# 10.) What is the oldest date in the to_date column?
# =============================================================================
dates = title_df['to_date'].sort_values()
oldest = dates.head(1)
#Ans: 1985-03-01
# =============================================================================
# 11.)What is the most recent date in the to_date column?
# =============================================================================
dates1 = title_df['to_date'].sort_values()
most_recent = dates1.tail(1)
#Ans: 9999-01-01 I assume this means current empl
# =============================================================================
# 
# =============================================================================
# #                           ADVANCED DF EXERCISES PART 2
# =============================================================================
# 1.)Copy the users and roles DataFrames from the examples above.
# 
#2.) What is the result of using a right join on the DataFrames?
# =============================================================================
import pandas as pd
import numpy as np

users = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]})



roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
new_df = users.merge(roles, left_on='role_id', right_on='id', how='right')

# =============================================================================
#3.) What is the result of using an outer join on the DataFrames?
# =============================================================================
outer_df = users.merge(roles, left_on='role_id', right_on='id', how='outer')


# =============================================================================
# 4.)What happens if you drop the foreign keys from the DataFrames and try to merge them?
# =============================================================================

no_fk = users.merge(roles, left_on=None, right_on=None, how='inner', indicator=(True))
#Ans: returns nothing in the table

# users.drop(columns="role_id").merge(roles, how="outer, on="id)
# =============================================================================
#5.) Load the mpg dataset from PyDataset.
# ==========================================================================
from pydataset import data

mpg = data('mpg')
#showdoc=True

# =============================================================================
#6.)Output and read the documentation for the mpg dataset.
# =============================================================================
import numpy as np
import pandas as pd


mpg.info()

mpg.describe()
# =============================================================================
# 7.)How many rows and columns are in the dataset?
# =============================================================================
mpg.shape
#Ans: 234 columns, 11 rows
#rows, columns = df.shape ROWS FIRST, THEN COLUMNS

# =============================================================================
# 8.)Check out your column names and perform any cleanup you may want on them.
# =============================================================================
clean_mpg = mpg.rename(columns={'displ': 'display', 'cyl': 'cylinder',
                                'trans': 'transmission', 'drv': 'drive',
                                'cty': 'city_mpg', 'hwy': 'highway_mpg', 'fl': 'fuel'})

# =============================================================================
# 9.)Display the summary statistics for the dataset.
# =============================================================================
clean_mpg.info()
clean_mpg.describe()

# =============================================================================
# 10.) How many different manufacturers are there?
# =============================================================================
diff_man = clean_mpg.groupby('manufacturer').sum()
#Ans: 15 diff manufacturers
#alt method:            
# clean_mpg.manufacturer.unique().size

# =============================================================================
# 11.) How many different models are there?
# =============================================================================
diff_mods = clean_mpg.groupby('model').sum()
#Ans: 38 diff mods

# =============================================================================
# 12.)Create a column named mileage_difference like you did in the DataFrames 
# exercises; this column should contain the difference between highway and city 
# mileage for each car.
# =============================================================================
mileage_difference = clean_mpg['highway_mpg'] - clean_mpg['city_mpg']


clean_mpg['mileage_difference'] = mileage_difference

# =============================================================================
# 13.) Create a column named average_mileage like you did in the DataFrames exercises;
#     this is the mean of the city and highway mileage.
# =============================================================================
average_mileage = clean_mpg[['highway_mpg', 'city_mpg']].mean(axis=1)

clean_mpg['average_mileage'] = average_mileage

# =============================================================================
# 14.) Create a new column on the mpg dataset named is_automatic that holds boolean
#     values denoting whether the car has an automatic transmission.
# =============================================================================
def is_auto(row):
    if 'auto' in row:
        return True
    else:
        return False

auto = [is_auto(car) for car in clean_mpg['transmission']]
auto = pd.Series(auto)
auto.index = clean_mpg.index

clean_mpg['is_automatic'] = auto


# =============================================================================
# 15.) Using the mpg dataset, find out which which manufacturer has the best miles
#     per gallon on average?
# =============================================================================
best_man = clean_mpg.groupby('manufacturer')['average_mileage'].mean().sort_values().tail(1)
#Ans: honda, 28.5 average mpg

# =============================================================================
# 16.) Do automatic or manual cars have better miles per gallon?
# =============================================================================
best_tran = clean_mpg.groupby('is_automatic')['average_mileage'].mean().sort_values()
#Ans: manual is better
# =============================================================================
#                             EXERCISES PT 3
# =============================================================================
# =============================================================================
# 1.)Use your get_db_url function to help you explore the data from the chipotle database.
# =============================================================================

def get_db_url(user, host, password, database, query):
    
    url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
    
    return pd.read_sql(query, url)

chip_df = get_db_url(user, host, password, 'chipotle', 'select * from orders')

chip_df.head()


# =============================================================================
# 2.)What is the total price for each order?
# =============================================================================
def stripper(row):
    row = row.replace('$', '')
    row = row.replace(',', '')
    return float(row) 

chip_df['item_price'] = pd.Series([stripper(price) for price in chip_df['item_price']]) 


chip_df['total_price'] = chip_df['quantity'] * chip_df['item_price']

# =============================================================================
# 3.)What are the most popular 3 items?
# =============================================================================
popular = chip_df.groupby('item_name')['quantity'].sum().sort_values().tail(3)
#Ans: chips and guac, chicken burrito, chicken bowl




# =============================================================================
# 4.)Which item has produced the most revenue?
# =============================================================================
money_makers = chip_df.groupby('item_name')['total_price'].sum().head(1)
#Ans: six pack soft drink $369.63


# =============================================================================
# 5.)Join the employees and titles DataFrames together.
# =============================================================================
title_df = title_df.set_index('emp_no')
emp_df = emp_df.set_index('emp_no')
titemp_df = pd.concat([title_df, emp_df], axis=1)
titemp_df = titemp_df.dropna()
titemp_df.tail(10)


# =============================================================================
# 6.)For each title, find the hire date of the employee that was hired most recently 
#   with that title.
# =============================================================================
most_recent = titemp_df.groupby('title')['hire_date'].max()

# =============================================================================
# 7.)Write the code necessary to create a cross tabulation of the number of titles 
#     by department. (Hint: this will involve a combination of SQL code to pull 
#     the necessary data and python/pandas code to perform the manipulations.)
# =============================================================================





