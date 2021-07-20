#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:51:22 2021

@author: carolyndavis
"""

from pydataset import data
import numpy as np
import pandas as pd

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

grade_book = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


pd.core.frame.DataFrame


# =============================================================================
# 
# 1a.)Create a column named passing_english that indicates whether each student has a 
# passing grade in english.
# =============================================================================


grade_book['passing_english'] = grade_book.english >= 70


# =============================================================================
# 1b.) Sort the english grades by the passing_english column. How are duplicates handled?
# =============================================================================

grade_book = grade_book.sort_values(by='english', ascending = False)

# =============================================================================
# 
# 1c)Sort the english grades first by passing_english and then by student name. 
# All the students that are failing english should be first, and within the students 
# that are failing english they should be ordered alphabetically. The same should 
# be true for the students passing english. (Hint: you can pass a list to the 
# .sort_values method)
# =============================================================================
grade_book.sort_values([('passing_english'), ('name')])

# =============================================================================
# 
# Sort the english grades first by passing_english, and then by the actual english grade,
#  similar to how we did in the last step.
# =============================================================================
grade_book = grade_book.sort_values([('passing_english'), ('english')], ascending = False)


# =============================================================================
# Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.
# =============================================================================
avg_grade = grade_book[['math', 'english', 'reading']]

avg_grade = avg_grade.mean(axis=1)

grade_book["avg_grade"] = avg_grade


# =============================================================================
# Load the mpg dataset. Read the documentation for the dataset and use it for the 
# following questions:
# =============================================================================

mpg = data('mpg')

# =============================================================================
# How many rows and columns are there?
# =============================================================================

mpg.info()

#ans: 11 columns//234 rows


# =============================================================================
# What are the data types of each column?
# =============================================================================
 #                                    DATA TYPE
 # 0   manufacturer  234 non-null    object 
 # 1   model         234 non-null    object 
 # 2   displ         234 non-null    float64
 # 3   year          234 non-null    int64  
 # 4   cyl           234 non-null    int64  
 # 5   trans         234 non-null    object 
 # 6   drv           234 non-null    object 
 # 7   cty           234 non-null    int64  
 # 8   hwy           234 non-null    int64  
 # 9   fl            234 non-null    object 
 # 10  class         234 non-null    object
 
# =============================================================================
#  Summarize the dataframe with .info and .describe
# =============================================================================
mpg.describe()


# =============================================================================
# Rename the cty column to city.
# =============================================================================
mpg = mpg.rename(columns={'cty': 'city'})

# =============================================================================
# Rename the hwy column to highway.
# =============================================================================
mpg = mpg.rename(columns={'hwy': 'highway'})

# =============================================================================
# Do any cars have better city mileage than highway mileage?
# =============================================================================
mpg['city'] = mpg.city < mpg.highway
#Ans: none
# =============================================================================
# 
# Create a column named mileage_difference this column should contain the difference 
# between highway and city mileage for each car
# =============================================================================
mpg['mileage_difference'] = mpg['highway'] - mpg['city']


# =============================================================================
# Which car (or cars) has the highest mileage difference?
# =============================================================================

max_index = mpg[mpg['mileage_difference'] == mpg["mileage_difference"].max()]
#ans: 2 results

# =============================================================================
# Which compact class car has the lowest highway mileage? The best?
# =============================================================================
min_index = mpg[mpg['mileage_difference'] == mpg["mileage_difference"].min()]
#ans: 5 results

# =============================================================================
# Create a column named average_mileage that is the mean of the city and highway mileage
# =============================================================================
avg_mpg = mpg[['city', 'highway']]

avg_mpg = avg_mpg.mean(axis=1)

mpg["avg_mileage"] = avg_mpg


# =============================================================================
# Which dodge car has the best average mileage? Whats worst?
# =============================================================================

dodge = mpg[mpg['manufacturer'] == 'dodge']

max_dodge = dodge[dodge['avg_mileage'] == dodge['avg_mileage'].max()]

min_dodge = dodge[dodge['avg_mileage'] == dodge['avg_mileage'].min()]

# =============================================================================
# 
# Load the Mammals dataset. Read the documentation for it, and use the data to answer 
# these questions:
# =============================================================================
data('Mammals')
mammals = data('Mammals')


# =============================================================================
# How many rows and columns are there?
# =============================================================================
mammals.shape
#ans: 107, 4

# =============================================================================
# What are the data types?
# =============================================================================
mammals.info()
#Ans: floats and bools

# =============================================================================
# Summarize the dataframe with .info and .describe
# =============================================================================
mammals.info()
mammals.describe()


# =============================================================================
# What is the the weight of the fastest animal?
# =============================================================================

max_speed = mammals[mammals['speed'] == mammals["speed"].max()]
#Ans: weight = 55


# =============================================================================
# What is the overal percentage of specials?
# =============================================================================
avg_percentage = mammals['specials'].mean()
#Ans: .09


# =============================================================================
# How many animals are hoppers that are above the median speed? What percentage is this?
# =============================================================================
med_speed = mammals['speed'].median()
hopper = mammals[['hoppers', 'speed']]
hopper = hopper[hopper['hoppers'] == True]
fast_hopper = hopper[hopper['speed'] > med_speed]

perc = len(fast_hopper) / len(mammals)