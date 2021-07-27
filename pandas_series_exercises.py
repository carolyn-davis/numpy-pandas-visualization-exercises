#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:51:27 2021

@author: carolyndavis
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
fruits_series.str.apply(lambda n: 'o' > 1)
# =============================================================================
# # 6.) Write the code to get only the string values containing the substring "berry".
# =============================================================================
#fruits_series.str.contains('berry')

fruits_series.str.findall('berry')
#Ans: 4 results for berry at indexes: 2,13,14,15
# =============================================================================
# # 7.) Write the code to get only the string values containing the substring "apple".
# =============================================================================
fruits_series.str.findall('apple')
#Ans: 3 results for apple at indexes: 3,4,5
# =============================================================================
# # 8.) Which string value contains the most vowels?
# =============================================================================
def max_char_count(string):
    max_char = ''
    max_count = 0
    for char in set(string):
        count = string.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    return max_char

# print(max_char_count('apple'))


fruits_series.apply(max_char_count(fruits_series))



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
vowels = letter_series.str.count(r'[aeiou]').sum()
#Ans: sum is 34

# =============================================================================
# How many consonants are in the Series?
# =============================================================================
consonants = len(letter_series) - vowels

#ans: 166

# =============================================================================
# Create a Series that has all of the same letters but uppercased.
# =============================================================================
new_letter_series = pd.Series([letter.upper() for letter in letter_series], name= 'Big Letters')

# =============================================================================
# 
# Create a bar plot of the frequencies of the 6 most commonly occuring letters.
# =============================================================================
to_plot = letter_series.value_counts()

to_plot = to_plot.head(6)

to_plot.plot.bar()
plt.show()
plt.close()

# =============================================================================
# Use PANDAS to create a Series named numbers from the following list:
# =============================================================================
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98',
                     '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45',
                     '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17',
                     '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54',
                     '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# =============================================================================
# 1.)What is the data type of the numbers Series?
# ============================================================================
for row in numbers:
    print(type(row))
#Ans: strings

# =============================================================================
# 
# 2.)How many elements are in the number Series?
# =============================================================================
len(numbers)
#Ans: 20

# =============================================================================
# 3.)Perform the necessary manipulations by accessing Series attributes and methods 
# to convert the numbers Series to a numeric data type.
# =============================================================================
numbers = [number.replace('$', '') for number in numbers]

numbers = [float(number.replace(',', '')) for number in numbers]
numbers = pd.Series(numbers)


# =============================================================================
# 4.)Run the code to discover the maximum value from the Series.
# =============================================================================
max(numbers)
#Ans: 4789988.17

# =============================================================================
# 5.)Run the code to discover the minimum value from the Series.
# =============================================================================
min(numbers)
#Ans: 278.6

# =============================================================================
# 6.)What is the range of the values in the Series?
# =============================================================================
range_num = max(numbers) - min(numbers)
print(range_num)
#Ans: 4789709.57

# =============================================================================
# 7.)Bin the data into 4 equally sized intervals or bins and output how many values 
# fall into each bin.
# =============================================================================
bins = range_num.value_counts(bins=4)



# =============================================================================
# 8.)Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
# =============================================================================
bins.plot()


# =============================================================================
# Use pandas to create a Series named exam_scores from the following list:
# =============================================================================

# =============================================================================

# =============================================================================
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69,
                         81, 96, 80, 85, 92, 82, 78])

# =============================================================================
# 1.)How many elements are in the exam_scores Series?
# =============================================================================
len(exam_scores)
#ans: 20

# =============================================================================
# 2.)Run the code to discover the minimum, the maximum, the mean, and the median scores 
# for the exam_scores Series.
# =============================================================================
scores = exam_scores.describe()
medians = pd.Series(exam_scores.median(), name="median")
scores = pd.concat([scores, medians], axis=0)#includes median on the summary describe() gave me
scores = scores.rename(index={0:'median'}) 


# =============================================================================
# 3.)Plot the Series in a meaningful way and make sure your chart has a title and 
#     axis labels.
# =============================================================================
import matplotlib.pyplot as plt

exam_scores.plot.bar(edgecolor='black')
plt.title('Exam Scores')
plt.ylabel('Scores')
plt.xlabel('Student ID')
plt.show()


# =============================================================================
# 4.)Write the code necessary to implement a curve for your exam_grades Series and 
# save this as curved_grades. Add the necessary points to the highest grade to 
# make it 100, and add the same number of points to every other score in the Series 
# as well.
# =============================================================================

curve = 100 - exam_scores.max()
curved_grades = pd.Series([i + curve for i in exam_scores])

# =============================================================================
# 
# 5.)Use a method to convert each of the numeric values in the curved_grades Series 
#     into a categorical value of letter grades. For example, 86 should be a 'B' and 
#     95 should be an 'A'. Save this as a Series named letter_grades.
# =============================================================================
rubric = {'A': [i for i in range(90, 101)],
                 'B': [i for i in range(80, 90)],
                 'C': [i for i in range(70, 80)],
                 'F': [i for i in range(0, 70)]}

# letter_grades = [key for key, value in rubric.items() if ]

letter_grades = []
for grade in curved_grades:
    for key, value in rubric.items():
        if grade in value:
            letter_grades.append(key)

letter_grades = pd.Series(letter_grades, name='letter')
letter_grades = pd.DataFrame(letter_grades)

# =============================================================================
# 6.)Plot your new categorical letter_grades Series in a meaninful way and include 
# a title and axis labels.
# =============================================================================
groups = letter_grades.value_counts().sort_index().plot.bar(edgecolor='black')
plt.title('Student Grades By Letter')
plt.ylabel('Scores')
plt.xlabel('Letter')
plt.show()