# https://leetcode.com/problems/same-tree/

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            if root1.val != root2.val:
                return False
            return helper(root1.left, root2.left) and helper(root1.right, root2.right)
        return helper(p, q)
