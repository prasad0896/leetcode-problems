# -*- coding: utf-8 -*-
"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Created on Sat Sep  7 13:46:59 2019

@author: prasa
"""
def getRow(rowIndex) -> List[int]:
    triangle = dict()
    triangle[0] = [1]
    triangle[1] = [1,1]
    triangle[2] = [1,2,1]
    for i in range(3, rowIndex+1):
        row = [1]
        for j in range(1,i):
            row.append(triangle[i-1][j]+triangle[i-1][j-1])
        row.append(1)
        triangle[i] = row
        #print(triangle)
    return triangle[rowIndex]
        
