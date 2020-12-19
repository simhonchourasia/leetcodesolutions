# https://leetcode.com/problems/first-missing-positive/

class Solution:
    # Takes n log n time, where n is the number of positive integers in the original list
    # This is because we use Python's sort, which is O(n log n)
    # If we used radix sort, though, we can do this in O(n log 2^32) = O(32n) ~ O(n) time
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = [x for x in nums if x > 0]
        positives = sorted(positives)
        if len(positives) == 0:
            return 1
        if positives[0] > 1:
            return 1
        for i in range(len(positives)-1):
            if positives[i+1]-positives[i] > 1:
                return positives[i]+1
        return positives[-1]+1
