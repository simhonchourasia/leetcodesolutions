# https://leetcode.com/problems/merge-two-binary-trees/

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # If there is no t1 or t2, return the other one
        if t1==None:
            return t2
        if t2==None:
            return t1

        # Merge the root
        t1.val += t2.val
        # Recursively merge the left and right subtrees
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# Time Complexity: O(M+N) where M,N are number of nodes in the trees, 
# since we only go through each node once
