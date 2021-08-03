#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:50:30 2021

@author: carolyndavis
"""
# =============================================================================
#                         SEABORN EXERCISES
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# 1.)Use the iris database to answer the following quesitons:
# =============================================================================

iris_df = sns.load_dataset('iris')


# =============================================================================
# 1.)What does the distribution of petal lengths look like?
# =============================================================================
#histplot
petal_length_dist = sns.histplot(iris_df.petal_length)

plt.show()


# =============================================================================
# 2.)Is there a correlation between petal length and petal width?
# =============================================================================
x = iris_df['petal_length']
y = iris_df['petal_width']
z = x.corr(y)


# =============================================================================
# 3.)Would it be reasonable to predict species based on sepal width and sepal length?
# =============================================================================


# iris_df.plot.scatter(x='sepal_width', y='sepal_length')

setosa = iris_df[iris_df['species'] == 'setosa']
versicolor = iris_df[iris_df['species'] == 'versicolor']
virginica = iris_df[iris_df['species'] == 'virginica']

ax=plt.gca()

ax.scatter(data=setosa, x='sepal_width', y='sepal_length', color= 'blue', label= 'setosa')

ax.scatter(data=versicolor, x='sepal_width', y='sepal_length', color= 'red', label= 'versicolor')
ax.scatter(data=virginica, x='sepal_width', y='sepal_length', color= 'green', label= 'virginica')

plt.legend(bbox_to_anchor=(1.0, 0.5))
plt.show()
plt.close()
#Ans: based off data, no, too many shared sepal characteristics among species
# =============================================================================
# 4.)Which features would be best used to predict species?
# =============================================================================
x = iris_df['petal_length']
y = iris_df['petal_width']
z = x.corr(y)

a = iris_df['sepal_length']
b = iris_df['sepal_width']
c = a.corr(b)

#Ans: Sepal features would be best due to their inverse correlation

# =============================================================================
# 1.) Using the lesson as an example, use seaborn's load_dataset function to load the 
# anscombe data set. Use pandas to group the data by the dataset column, and 
# calculate summary statistics for each dataset. What do you notice?
# 
# Plot the x and y values from the anscombe data. Each dataset should be in a 
# separate column.
# =============================================================================

anscombe_df = sns.load_dataset('anscombe')

group_x = anscombe_df.groupby("dataset")["x"].describe()
group_y = anscombe_df.groupby("dataset")["y"].describe()

sns.relplot(x='x', y='y', data=anscombe_df, col="dataset")
plt.suptitle("x & y plots for Anscombe Data")
plt.show()



# =============================================================================
# 2.)Load the InsectSprays dataset and read it's documentation. Create a boxplot that
#  shows the effectiveness of the different insect sprays.
# =============================================================================
from pydataset import data

insect_sprays = data('InsectSprays')

bp = sns.boxplot(x='spray', y='count', data=insect_sprays)




# =============================================================================
# 3.)Load the swiss dataset and read it's documentation. The swiss dataset is available
#  from pydatset rather than seaborn. Create visualizations to answer the following 
#  questions:
# =============================================================================
swiss_df = data('swiss')


# =============================================================================
# Create an attribute named is_catholic that holds a boolean value of whether or not
#  the province is Catholic. (Choose a cutoff point for what constitutes catholic)
# =============================================================================
med = swiss_df['Catholic'].median()
def_catholic = swiss_df[swiss_df['Catholic']> med]

is_catholic = []
for value in swiss_df.index:
    if value in def_catholic.index:
        is_catholic.append(True)
    else:
        is_catholic.append(False)
        
is_catholic = pd.Series(is_catholic, name="is_catholic")
is_catholic.index = swiss_df.index
swiss_df.loc[:,'is_catholic'] = is_catholic

# =============================================================================
# Does whether or not a province is Catholic influence fertility?
# =============================================================================
fertilit = swiss_df['Catholic'].corr(swiss_df['Fertility'])
#Ans: Corr of .46//medium correlation 


# =============================================================================
# What measure correlates most strongly with fertility?
# =============================================================================
matrix = swiss_df.corr()
#Ans: education is the strongest indicator with an inverse correlation of -0.66


# =============================================================================
# 4.)Using the chipotle dataset from the previous exercise, create a bar chart that 
# shows the 4 most popular items and the revenue produced by each.
# =============================================================================


import pandas as pd
import numpy as np

from env import host, user, password


def get_db_url(user, host, password, database, query):
    
    url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
    
    return pd.read_sql(query, url)



# =============================================================================
# 5.)Load the sleepstudy data and read it's documentation. Use seaborn to create 
#     a line chart of all the individual subject's reaction times and a more 
#     prominant line showing the average change in reaction time.
# =============================================================================
sleep_study = data("sleepstudy")

sleep_wide = sleep_study.pivot("Subject", "Days", "Reaction")

plot = sns.lineplot(data=sleep_wide.T)
plot.legend(loc='upper left', bbox_to_anchor=(1, 1))






