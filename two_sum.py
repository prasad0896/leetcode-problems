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
        for i in nums:
            subtraction = target - i
            try:
                index1 = nums.index(i)
                index2 = nums.index(subtraction)
                return [index1,index2]
            except:
                pass
        
