# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Create list to hold values
        T = [0 for i in range(max(3, n+1))]
        # Set up base cases
        T[0]=0
        T[1]=1
        T[2]=1
        # Use previous values to calculate and memoize next value
        for i in range(3, n+1):
            # 
            T[i]=T[i-1]+T[i-2]+T[i-3]
        return T[n]

# Time complexity: O(N)
