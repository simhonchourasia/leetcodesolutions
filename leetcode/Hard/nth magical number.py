# https://leetcode.com/problems/nth-magical-number/

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        M = 1000000007
        # Define gcd and lcm helper functions
        def gcd(a, b):
            while b > 0:
                a, b = b, a%b
            return a
        def lcm(a, b):
            return a*b/gcd(a,b)

        L = lcm(A, B)
        X = L/A
        Y = L/B
        q = N // (X+Y-1)
        r = N%(X+Y-1)
        if r==0:
            return q*L%M
        nxt = [A, B]
        for i in range(r-1):
            if nxt[0] <= nxt[1]:
                nxt[0] += A
            else:
                nxt[1] += B
        A = min(nxt)
        return (q*L+A)%M
