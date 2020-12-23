# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        S = sorted(nums)
        i = 0
        while i < len(S):
            if i == len(S) - 1:
                return S[i]
            if S[i] == S[i+1]:
                i += 3
            else:
                return S[i]
