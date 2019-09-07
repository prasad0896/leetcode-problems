# -*- coding: utf-8 -*-
"""
Code to find first unique character in string
Created on Sat Sep  7 09:28:37 2019

@author: prasa
"""

def firstUniqChar(s) -> int:
    char_items = list(s) 
    dictionary = {}

    for index,character in enumerate(char_items): 
        if character not in dictionary.keys():
            dictionary[character] = []
        dictionary[character].append(index)
        
    for i in char_items:
        if len(dictionary[i]) == 1:
            return dictionary[i][0]
    return -1