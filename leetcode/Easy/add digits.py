# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Equivalent to finding the sum of digits
        # We need to take special cases for when the original number is 0
        if num==0:
            return 0
        # And another special case for when the sum of digits is divisible by 9
        if num%9==0:
            return 9
        # Otherwise, it is just the sum of digits, which is equal to the number % 9
        return num%9

