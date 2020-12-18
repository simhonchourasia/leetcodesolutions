# https://leetcode.com/problems/k-th-symbol-in-grammar/

# We make the observation that row n+1 contains the elements of row n, 
# followed by the elements of row n but inverted

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 and K == 1: # Base case
            return 0
        if K > 2**(N-2): # Inverted corresponding row n
            return 1 - self.kthGrammar(N-1, K - 2**(N-2))
        else:
            return self.kthGrammar(N-1, K)
