# https://leetcode.com/problems/permutation-sequence/

class Solution:
    
    
    def getPermutation(self, n: int, k: int) -> str:
        nums = [x+1 for x in range(n)]
        factorial = [1]
        for i in range(1, 10):
            factorial.append(factorial[-1]*i)
        def helper(ret, rem, m):
            if len(rem) == 0: # If there are no numbers remaining to permute
                return ret
            # Perform division with remainder
            r = m % factorial[len(rem)-1]
            q = m // factorial[len(rem)-1]
            ret += str(rem[q])
            # Remove the number we used
            return helper(ret, rem[:q]+rem[q+1:], r)
        return helper("", nums, k-1)
