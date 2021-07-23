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