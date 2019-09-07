# -*- coding: utf-8 -*-
"""
Moving zeroes in place (hacked solution)
Created on Sat Sep  7 17:11:54 2019

@author: prasa
"""

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    ne = []
    while i < len(nums):
        if nums[i] != 0:
            ne.append(nums[i])
        i += 1
    ne.extend([0]*(len(nums) - len(ne)))
    #print(ne)
    for i in range(len(nums)):
        nums[i] = ne[i]
