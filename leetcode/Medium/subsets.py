# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Helper function to get the binary string representation of a number
        def getBinary(n):
            return bin(n)[2:]
        
        powerset = []
        N = len(nums)
        # Go across all the bitmasks from 2^N to 2^(N+1)
        for i in range(1 << N, 1 << (N+1)):
            subset = []
            b = getBinary(i)[1:]
            for j in range(N):
                # If the corresponding bit is 1, add the element of nums to the subset
                if b[j]=='1':
                    subset.append(nums[j])
            powerset.append(subset)
        return powerset

# Time complexity: O(2^N), where N is the number of elements in nums
