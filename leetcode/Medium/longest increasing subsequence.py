# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums);
        if N==0:
            return 0
        # Create DP table where dp[i] represents the length of the longest increasing subsequence using nums[:i]
        dp = [1 for i in range(N)]
        for i in range(1, N):
            for j in range(i):
                if nums[i]>nums[j]:
                    # Take the maximum of all dp[j]+1 for j in the interval [0, i-1]
                    dp[i]=max(dp[i], dp[j]+1)
                
        return max(dp)

# Time Complexity: O(N^2), as we have two for loops which run O(N) times each
