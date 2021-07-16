#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:51:27 2021

@author: carolyndavis
"""

import numpy as np
import pandas as pd
# =============================================================================
#                            EXERCISES PART 1:
# =============================================================================
fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits_series = pd.Series(fruits)
fruits_series 


# =============================================================================
# Determine the number of elements in fruits.
# =============================================================================
print(len(fruits_series))

#fruits.size()
#fruits.shape()  #returns column of 17 rows



# =============================================================================
# Output only the index from fruits.
# =============================================================================
print(fruits_series.index)


# =============================================================================
# Output only the values from fruits.
# =============================================================================

print(fruits_series.values)

#fruits_series.index.tolist()
#values.tolist()

# =============================================================================
# Confirm the data type of the values in fruits.
# =============================================================================
type(fruits_series.values)

# =============================================================================
# Output only the first five values from fruits. Output the last three values. 
# Output two random values from fruits.
# =============================================================================
fruits_series.head(5)  #by default returns 5

fruits_series.tail(3)

fruits_series.sample(2)

# =============================================================================
# Run the .describe() on fruits to see what information it returns when called on a 
# Series with string values.
# =============================================================================
#depends onn what kind of datatypes are in series
fruits_series.describe()
type(fruits_series.describe())
# =============================================================================
# Run the code necessary to produce only the unique string values from fruits
# =============================================================================

fruits_series.unique()  #returns array of just unique values
#fruit_series.nunique.() returns count of unique values 
# =============================================================================
# Determine how many times each unique string value occurs in fruits.
# =============================================================================
fruits_series.value_counts()
#fruits.value_counts().head(1)

#fruits.value_counts().idmax() #returns the first occurance works only if no dupes

#fruits.value_counts.nlargest(n=1, keep='all')


# =============================================================================
# Determine the string value that occurs most frequently in fruits.
# =============================================================================

fruits_series.value_counts().tail(11)

# =============================================================================
#                                 EXERCISES PART 2:
# =============================================================================


# =============================================================================
# # Capitalize all the string values in fruits.
# =============================================================================
fruits_series.str.capitalize()




# =============================================================================
# # 1.) Count the letter "a" in all the string values (use string vectorization).
# =============================================================================
fruits_series.str.count('a')
# =============================================================================
# # 2.) Output the number of vowels in each and every string value.
# =============================================================================

def vowel_counter(value, letter):
    x = value.count(letter)
    return x

vowels = ['a', 'e', 'i', 'o', 'u']

collector = {}
for row in fruits_series:
    collector[row] = {}
    for letter in vowels:
        collector[row][letter] = vowel_counter(row, letter)

# =============================================================================
# # 3.) Write the code to get the longest string value from fruits.
# =============================================================================
def get_max_str(fruit_series):
    return max(fruits_series, key=len)

get_max_str(fruits_series)   #honeycrisp apple
# =============================================================================
# # 4.) Write the code to get the string values with 5 or more letters in the name.
# =============================================================================
# for i in fruits_series: 
#     if len(i) >= 5:
#         print(i)


max(fruits,key=len)             
            
# =============================================================================
# # 5.) Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
# =============================================================================
fruits_series.apply(lambda n: 'o' > 1)
# =============================================================================
# # 6.) Write the code to get only the string values containing the substring "berry".
# =============================================================================
#str.contains method
# =============================================================================
# # 7.) Write the code to get only the string values containing the substring "apple".
# =============================================================================
#str.contains
# =============================================================================
# # 8.) Which string value contains the most vowels?
# =============================================================================
#str.count///nlargest


# =============================================================================
#                             EXERCISES PART 3:
# =============================================================================

def split(letters):
    return [char for char in letters]

letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
split_list = (split(letters))
print(split_list)

letter_series = pd.Series(split_list)
letter_series
type(letter_series)
# =============================================================================
# Which letter occurs the most frequently in the letters Series?
# =============================================================================
import collections
max_freq = letter_series
count =collections.Counter(letter_series)
print(str(max(count, key = count.get)))
#Ans: y

# =============================================================================
# Which letter occurs the Least frequently?
# =============================================================================

min_freq = letter_series
count =collections.Counter(letter_series)
print(str(min(count, key = count.get)))
#Ans: letter 'l'

# =============================================================================
# How many vowels are in the Series?
# =============================================================================
letter_series.str.count(r'[aeiou]').sum()
#Ans: sum is 34

# =============================================================================
# How many consonants are in the Series?
# =============================================================================
letter_series.str.count(r'[aeiou]').sum()