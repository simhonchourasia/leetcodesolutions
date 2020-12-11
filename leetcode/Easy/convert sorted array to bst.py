# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution:

    # Time complexity: O(n)
    # Recursively calls to form left and right subtrees
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return None
        mid = len(nums)//2
        return TreeNode(val = nums[mid], left = self.sortedArrayToBST(nums[:mid]), right = self.sortedArrayToBST(nums[mid+1:]))
