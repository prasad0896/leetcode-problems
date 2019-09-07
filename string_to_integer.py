# -*- coding: utf-8 -*-
"""
String to integer

@author: prasad
"""
def myAtoi(str) -> int:
    str = str.strip()
    max_size = (2**31)-1
    min_size = -1 * (2**31)
    result = ''
    i = 0
    while i<len(str):
        if str[i]==' ':
            i+=1
        else:
            break
            
    str=str[i:]
    
    for i in range(len(str)):
        if i == 0 and str[i] in '+-':
            result += str[i]
        elif str[i].isnumeric():
            result += str[i]
        else:
            break
            
    if len(result) == 1 and not result[0].isnumeric():
        return 0
    
    if result:
        result = int(result)
        if result >= min_size and result <= max_size:
            return result
        elif result < min_size:
            return min_size
        else:
            return max_size
    else:
        return 0
