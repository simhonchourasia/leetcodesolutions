# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Finds if a number n is prime
        # Runs in O(sqrt(n)) time
        def isPrime(n):
            if n == 1:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        def getFactors(n):
            ret = []
            for i in range(1, n+1):
                if n % i == 0:
                    ret.append(i)
            return ret
        def getPrimeFactors(n, acc):
            if isPrime(n):
                acc.append(n)
                return acc
            i = 2
            while i*i <= n:
                if n % i == 0:
                    acc.append(i)
                    return getPrimeFactors(n // i, acc)
                i += 1
                
        factors = getFactors(n)
        if k > len(factors):
            return -1
        return factors[k-1]
