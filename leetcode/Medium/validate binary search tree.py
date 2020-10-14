# https://leetcode.com/problems/validate-binary-search-tree/

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Keep track of lowest and highest possible values
        # Initially, low is "- infinity", high is "infinity"
        low = -1000000000000
        up = 1000000000000
        def helper(node, lower, upper):
            if node == None:
                return True
            # Validate current node
            if node.val<=lower or node.val >= upper:
                return False
            # Recursively call on left and right subtrees
            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, upper):
                return False
            return True
        return helper(root, low, up)
                
