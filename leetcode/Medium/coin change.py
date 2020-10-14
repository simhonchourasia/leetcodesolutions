# https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        intmax = 3000000000
        # Create DP array where dp[i] is the minimum number of coins to create amount i
        dp = [intmax for i in range(amount+1)]
        # Base case
        dp[0] = 0
        
        for c in coins:
            for i in range(c, amount+1):
                # Find the minimum using any coin
                dp[i] = min(dp[i], dp[i-c]+1)
        if dp[amount]==intmax:
            return -1
        return dp[amount]

# Time Complexity: O(A*C), where A is the amount and C is the number of coins
