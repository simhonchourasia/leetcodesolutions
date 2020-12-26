# https://leetcode.com/problems/balance-a-binary-search-tree/

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, acc):
            if node == None:
                return acc
            return inorder(node.left, [node.val] + inorder(node.right, acc))
        
        def listToBalanced(lst):
            N = len(lst)
            if N == 0:
                return None
            left = lst[:N//2]
            right = lst[N//2+1:]
            num = lst[N//2]
            return TreeNode(val=num, left=listToBalanced(left), right=listToBalanced(right))
        
        return listToBalanced(inorder(root, []))
