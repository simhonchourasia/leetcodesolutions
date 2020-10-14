# https://leetcode.com/problems/super-pow/

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # Parse the array and convert to integer
        # Only works here because Python allows arbitrarily large ints
        B = int("".join([str(x) for x in b]))
        # Euler's Theorem: phi(1337) = 1140, so a^1140 = 1
        B %= 1140
        return (a**B)%1337

# Time Complexity: O(S), where S is the length of the array B
