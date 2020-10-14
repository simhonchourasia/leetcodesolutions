# https://leetcode.com/problems/perfect-squares/

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize DP table with "infinity"
        # dp[i] is the least number of perfect squares which sum to i
        dp = [1000000000 for i in range(n+1)]
        # Base cases
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            # Try all perfect squares less than i
            j = 1
            while j*j <= i:
                # Find the minimum possible value for all j
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]

# Time complexity: O(n sqrt(n))
