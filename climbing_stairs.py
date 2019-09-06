'''
We store solution for base case and then approach dp for further cases
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        table = dict()
        table[0] = 0
        table[1] = 1
        table[2] = 2
        for i in range(3,n+1):
            table[i] = table[i-1] + table[i-2]
        return table[n]