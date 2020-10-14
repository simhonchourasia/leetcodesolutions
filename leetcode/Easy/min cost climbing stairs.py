# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        # Set up list with "infinitely" large costs
        # dp[i] represents the iminimum cost to reach step i
        dp = [10000000 for i in range(N+1)]
        # Base cases: step 0 and 1 are free
        dp[0] = 0
        dp[1] = 0
        for i in range(2, N+1):
            # Either we take 1 step from step i-1 or we take 2 steps from step i-2
            # So we greedily take the minimum
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[N]

# Time complexity: O(N), we only do one pass through the list of length N
