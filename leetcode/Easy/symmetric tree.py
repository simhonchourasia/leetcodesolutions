# https://leetcode.com/problems/symmetric-tree/

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node1, node2):
            # Base case
            if node1==None and node2==None:
                return True
            # If one is empty and the other is not
            if node1==None or node2==None:
                return False
            # Recursively call on left and right subtree
            ret = node1.val==node2.val and helper(node1.left, node2.right) and helper(node2.left, node1.right)
            return ret
        return helper(root, root)
