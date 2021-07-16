#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:31:08 2021

@author: carolyndavis
"""

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a[4]

# =============================================================================
# 1.) How many negative numbers are there?
# =============================================================================
a[a < 0].size
#Answer: 4


# =============================================================================
# 2.)How many positive numbers are there?
# =============================================================================
a[a > 0].size
#ans: 5
# =============================================================================
# 3.)How many even positive numbers are there?
# =============================================================================
evens = a[a % 2 == 0]
for i in range(len(evens)):
    if (evens[i] > 0):
        print(evens[i], end = " ")
#Answer: 4, 10, 12



# =============================================================================
# 4.)If you were to add 3 to each data point, 
#     how many positive numbers would there be?
# =============================================================================
array_plus_three = [n + 3 for n in a]
print(array_plus_three)

# =============================================================================
# 5.)If you squared each number, what would the new mean and standard deviation be?
# =============================================================================
array_squared = a ** 2  
 #squared 
array_mean = np.mean(array_squared)
print(array_mean)

array_std = np.std(array_squared)
#Answer 144.0243...


# =============================================================================
# 6.)A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.
# =============================================================================
mean_c = array_mean

std_c = array_std

centered_data = (std_c * array_squared) + mean_c
print(centered_data)

# =============================================================================
# 7.)Calculate the z-score for each data point. 
# =============================================================================
from scipy import stats

z_score = stats.zscore(centered_data)
print(z_score)


# =============================================================================
# 8.)                     MORE NUMPY PRACTICE
# =============================================================================
## Setup 1
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers 
#in above list

sum_of_a = sum(a1)
#Ans= 55

# =============================================================================
# # Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers 
# in the above list
# =============================================================================
min_of_a = min(a1)
#ans= 1

# =============================================================================
# # Exercise 3 - Make a variable named max_of_a to hold the max number of all the 
# numbers in the above list
# =============================================================================
max_of_a = max(a1)
#ans= 10
# =============================================================================
# # Exercise 4 - Make a variable named mean_of_a to hold the average of all the 
# numbers in the above list
# =============================================================================
mean_of_a = np.mean(a1)
#ans= 5.5

# =============================================================================
# # Exercise 5 - Make a variable named product_of_a to hold the product of multiplying 
# all the numbers in the above list together
# =============================================================================
product_of_a = np.prod(a1)
#ans= 3628800

# =============================================================================
# # Exercise 6 - Make a variable named squares_of_a. It should hold each number in a 
# squared like [1, 4, 9, 16, 25...]
# =============================================================================

squares_of_a = np.square(a1)


# =============================================================================
# # Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
# =============================================================================
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a1[a1 % 2 == 1]
print(odds_in_a)