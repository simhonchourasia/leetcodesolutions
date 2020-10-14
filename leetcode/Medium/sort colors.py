# https://leetcode.com/problems/sort-colors/

# Use counting sort because there are a very small (3) number of possibilities to sort
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        L = [0, 0, 0]
        for x in nums:
            # Essentially just finding how many 0s, 1s, 2s there are in the original list
            L[x] += 1
        k = 0
        for i in range(3):
            for j in range(L[i]):
                # Recreating the list (but sorted)
                nums[k] = i
                k += 1

# Time complexity: O(N), where N is the length of nums
# We only pass through nums once, and the for loop at the end performs a total of N loops

