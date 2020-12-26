# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a = 0
        b = 1
        fib = []
        while a < 1000000000:
            a, b = b, a+b
            fib.append(a)

            
        def helper(num, ret):
            if num == 0:
                return ret
            for i in range(len(fib)-1, -1, -1):
                if fib[i] <= num:
                    return helper(num - fib[i], ret + 1)
                
        return helper(k, 0)
                
