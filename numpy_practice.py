#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:38:49 2021

@author: carolyndavis
"""

import numpy as np



#Creating numpy arrays:
    #Numpy arrays go above an beyond what Python's built in lists can do:
a = np.array([1, 2, 3])
a


#We can created multi-dimensional arrays:
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
matrix


#Refrencing elements in numpy arrays == same as refrencing elements (python)

a[0]
#output is 1 because 1 is at index/position 0

print('a    == {}'.format(a))
print('a[0] == {}'.format(a[0]))
print('a[1] == {}'.format(a[1]))
print('a[2] == {}'.format(a[2]))

#To obtain an element from the second column in the second row:
    
matrix[1, 1]

#To get the first 2 elements if the last 2 rows:

matrix[1:, :2]

#Arrays can be indexed with a boolean sequence to indicate which values should be 
#included in the resulting array 

should_include_elements = [True, False, True]
a[should_include_elements]

#Note the boolean sequence length is the same length as the array being indexed


# =============================================================================
# VECTORIZED OPERATIONS
# =============================================================================
#If we wanted to add 1 to every element in a list, without numpy, 
#we might write a for loop or a list comprehension:

original_array = [1, 2, 3, 4, 5]
array_with_one_added = []
for n in original_array:
    array_with_one_added.append(n + 1)
print(array_with_one_added)

#Vectorizing operations means applying operations to ever element in 
#a vector, which the vector in our case: for numpy arrays: simply add 1

original_array = np.array([1, 2, 3, 4, 5])
original_array + 1

#his works the same way for the other basic arithmatic operators as well.

my_array = np.array([-3, 0, 3, 16])

print('my_array      == {}'.format(my_array))
print('my_array - 5  == {}'.format(my_array - 5))
print('my_array * 4  == {}'.format(my_array * 4))
print('my_array / 2  == {}'.format(my_array / 2))
print('my_array ** 2 == {}'.format(my_array ** 2))
print('my_array % 2  == {}'.format(my_array % 2))

#Not only are the arithmatic operators vectorized, 
#but the same applies to the comparison operators.
my_array = np.array([-3, 0, 3, 16])

print('my_array       == {}'.format(my_array))
print('my_array == -3 == {}'.format(my_array == -3))
print('my_array >= 0  == {}'.format(my_array >= 0))
print('my_array < 10  == {}'.format(my_array < 10))

#Getting all postive numbers in my_array:
my_array[my_array > 0]

#All even numbers:
my_array[my_array % 2 == 0]

# =============================================================================
# CREATING ARRAYS
# =============================================================================
# =============================================================================
# np.random.randn can be used to create an array of specified length 
# of random numbers drawn from the standard normal distribution.
# =============================================================================
np.random.randn(10)  #number in parenth, is the length/total number of output requsted

#We can also pass a second argument to this function to define the 
#shape of a two dimensional array.
np.random.randn(3, 4)
#3 rows of random numbers with shape of 4 columns


# =============================================================================
# #If we wish to draw from a normal distribution with mean 
# μ
#  and standard deviation 
# σ
# , we'll need to apply some arithmetic. Recall that to convert 
# from the standard normal distribution, we'll need to multiply by 
# the standard deviation, and add the mean.
# =============================================================================
mu = 100
sigma = 30

sigma * np.random.randn(20) + mu

# =============================================================================
# The zeros and ones functions provide the ability to create arrays of 
# a specified size full or either 0s or 1s, and the full function allows 
# us to create an array of the specified size with a default value.
# =============================================================================
print('np.zeros(3)    == {}'.format(np.zeros(3)))
print('np.ones(3)     == {}'.format(np.ones(3)))
print('np.full(3, 17) == {}'.format(np.full(3, 17)))


