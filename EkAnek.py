#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Problem - 1


# Consider the following series of binary numbers:
# 
# 11, 101, 110, 1001, 1010, 1100,...
# 
# All of these numbers have the same count of 1s.
# 
# Your job is to write a function that will accept the count of 1s, say k,  and another number N and return the binary string of Nth number with k 1s in it. For example for k = 2 and N= 5, this function should return 1010.
# 
# Your function signature should be similar to:
# 
# String getNthBinaryNumberWithKOnes(int k, int N)
# 

# In[ ]:


def constructString(ones, zeros, index, position):
    string = '1' + '0' * zeros + '1'* [ones -1]
    if position == index:
        return string
    ## construct strings here
    


# In[20]:


def getNthBinaryNumberWithKOnes(ones, position):
    string = '1' * ones
    zeros = 0
    index = 1
    if position == index:
        return string
    while True:
        zeros += 1
        temp, index = constructString(ones, zeros, index, position) #construct strings
        if position == index:
            return temp
        


# In[14]:


getNthBinaryNumberWithKOnes(3, 5)


# In[17]:


## Problem: 2


# You’re given an ordered set of n numbers (n is a power of 2). Initially all the numbers are zero. You’re supposed to perform a sequence of following online operations:
# 
# Add x to the ith entry
# Report the sum of numbers between indices i and j
# 
# It’s easy to see that if you store all these numbers in an array, the first operation can be performed in O(1) time but the second operation can take O(n) time in the worst case.
# 
# Our objective today is to perform these operations efficiently. Your job is to first create a data-structure which will guarantee better than O(n) time for both operations and then write the following two methods with the given signature:
# 
# void add(int index, int value)
# int sum(int startIndex, int endIndex)
# 
# Your data structure may have a simple initializer/constructor such as this:
# 
# My_custom_data_structure_instance = new MyCustomDataStructure(n)
# 

# In[ ]:


## new data structure to perform below operations
##O1: add value at given index
##O2: perform sum of ith index to jth index

class CustomDS(object):
    def __init__(self, n):
        self.length = n
        self.list = []
        self.sum = 0
    
    def sum(self, startIndex, endIndex):
        if ((endIndex - startIndex) > n // 2):
            diff = sum(self.list[0: startIndex]) + sum(self.list[endIndex: self.length-1])
            return self.sum - diff
        else:
            custom_sum = 0
            for i in range(startIndex, endIndex+1):
                custom_sum += self.list[i]
            return custom_sum
    
    def add(self, value, index):
        self.list[index] += value
        self.sum += value
        

