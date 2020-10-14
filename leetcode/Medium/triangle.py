# https://leetcode.com/problems/triangle/

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        N = len(triangle);
        # Initialize minimum path sums to "infinity"
        dp = [[10000000 for j in range(N)] for i in range(N)];
        # Base case
        dp[0][0] = triangle[0][0];
        for i in range(1,N):
            # Refer to past values to create current value (DP)
            dp[i][0] = dp[i-1][0] + triangle[i][0];
            dp[i][i] = dp[i-1][i-1] + triangle[i][i];
            for j in range(1, i):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j]);
        return min(dp[N-1])

# Time complexity: O(N^2)
