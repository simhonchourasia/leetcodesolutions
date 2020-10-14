# https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Common dynamic programming algorithm to find length of longest common subsequence
        # Runs in O(A*B) time, where A and B are the lengths of the sequences
        def lcs(S, T):
            A = len(S)
            B = len(T)
            # Create 2D DP table
            # dp[a][b] represents the longest common subsequence between first a chars of S and first b chars of T
            dp = [[0 for j in range(B+1)] for i in range(A+1)]
            for i in range(A+1):
                for j in range(B+1):
                    # Check if any are empty (first 0 chars of S or T)
                    if i*j==0:
                        dp[i][j] = 0
                    # If ith char of S is equal to jth char of T, we add 1
                    elif S[i-1]==T[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                    # Otherwise, we take the maximum of the previous cases
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[A][B]
        # Check if the length of the longest common subsequence is equal to the length of s
        return lcs(s,t)==len(s)
