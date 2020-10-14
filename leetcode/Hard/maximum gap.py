# https://leetcode.com/problems/maximum-gap/

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        S = sorted(nums)
        if N < 2:
            return 0
        mx = 0
        for i in range(N-1):
            if S[i+1]-S[i]>mx:
                mx = S[i+1]-S[i]
        return mx
    
# Time complexity: O(n log n), where n is the length of nums
