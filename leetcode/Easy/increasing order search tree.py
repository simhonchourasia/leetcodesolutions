# https://leetcode.com/problems/increasing-order-search-tree/

class Solution:
    # Tail-recursive in-order traversal of a BST, with complexity O(n) (where n = number of nodes)
    def inorder(self, root, acc):
        if root==None:
            return acc
        return self.inorder(root.left, [root.val] + self.inorder(root.right, acc))
    
    def toMaxHeightBST(self, lst, acc):
        if len(lst) == 0:
            return acc
        return self.toMaxHeightBST(lst[:-1], TreeNode(val = lst[-1], left = None, right = acc))
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = self.inorder(root, [])
        return self.toMaxHeightBST(lst, None)
        
