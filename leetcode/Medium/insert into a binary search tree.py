# https://leetcode.com/problems/insert-into-a-binary-search-tree/

class Solution:
    # Time complexity is O(h), where h is the height of the BST
    # This is because we only choose and traverse one subtree each time
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val=val, left=None, right=None)
        if val < root.val:
            return TreeNode(val = root.val, left = self.insertIntoBST(root.left, val), right = root.right)
        if val > root.val:
            return TreeNode(val = root.val, left = root.left, right = self.insertIntoBST(root.right, val))
