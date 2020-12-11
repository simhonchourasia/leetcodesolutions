# https://leetcode.com/problems/maximum-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def leftHelper(self, lst, acc):
        if len(lst) == 0:
            return acc
        return self.leftHelper(lst[:-1], TreeNode(val=lst[-1], right=acc))
    
    def rightHelper(self, lst, acc):
        if len(lst) == 0:
            return acc
        return self.rightHelper(lst[1:], TreeNode(val=lst[0], left=acc))
    
    
    def constructMaximumBinaryTree(self, nums):
        mx = max(nums)
        ind = nums.index(mx)
        leftNums = nums[:ind]
        rightNums = nums[ind+1:]
        return TreeNode(val=mx, left=self.leftHelper(leftNums, None), right=self.rightHelper(rightNums, None))
