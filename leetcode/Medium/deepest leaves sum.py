# https://leetcode.com/problems/deepest-leaves-sum/

class Solution:
    # Recursive function to find height of BST
    # Runs in O(n) time (where n is number of nodes)
    def heightBST(self, root):
        if root == None:
            return 0
        return 1 + max(self.heightBST(root.left), self.heightBST(root.right))
    
    # Helper function to do all of the processing
    # First check if the root is empty
    # Otherwise, it checks if the root is at the lowest level
    # Recursively calls itself on the left and right subtrees
    def helper(self, root, height, level):
        if root == None:
            return 0
        if level == height: 
            return root.val
        return self.helper(root.left, height, level+1) + self.helper(root.right, height, level+1)
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        height = self.heightBST(root)
        return self.helper(root, height, 1)
