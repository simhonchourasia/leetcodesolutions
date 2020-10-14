# https://leetcode.com/problems/unique-paths/

# We can create a bijection between the number of paths and the number of ways to permute m "downs" and n "rights"
# This is equal to ((m-1)+(n-1))!/((m-1)!(n-1)!), as the "downs" are indistinguishable and the "rights" are indistinguishable

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = m-1
        b = n-1
        # Create DP table for factorials, where dp[i] = i!
        factorial = [1 for i in range(a+b+1)]
        for i in range(1, a+b+1):
            factorial[i] = factorial[i-1]*i
        return factorial[a+b]/factorial[a]/factorial[b]

# Time Complexity: O(m+n), as running the loop for the factorial table takes O(m+n) steps
