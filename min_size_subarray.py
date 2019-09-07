# -*- coding: utf-8 -*-
"""
Given an array of n positive integers and a positive integer s, find 
the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.
Created on Sat Sep  7 13:09:42 2019

@author: prasa
"""
def minSubArrayLen(s, nums) -> int:
    current_sum = 0
    start_pointer = 0
    min_length = float('inf')
    for i in range(len(nums)):
        current_sum = current_sum + nums[i]
        while current_sum >= s:
            min_length = min(min_length, i-start_pointer+1)
            current_sum = current_sum - nums[start_pointer]
            start_pointer = start_pointer + 1
    if min_length == float('inf'):
        return 0
    return min_length

