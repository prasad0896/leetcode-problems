# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:28:21 2019

@author: prasa
"""
'''
Two sum:
Approach:
    Choose a number from the list
    subtract the number from the list (subtraction)
    Search subtraction in the list
    If found report 
    Else choose next number
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
