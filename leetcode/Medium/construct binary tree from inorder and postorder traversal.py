# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        val = postorder[-1]
        posIn = inorder.index(val)
        leftInorder = inorder[:posIn]
        rightInorder = inorder[posIn+1:]
        
        if len(rightInorder) == 0:
            leftPostorder = postorder[:-1]
            rightPostorder = []
        else:
            posPost = postorder.index(rightInorder[0])
            leftPostorder = postorder[:posPost]
            rightPostorder = postorder[posPost:-1]
        
        return TreeNode(val=val, left=self.buildTree(leftInorder, leftPostorder), right=self.buildTree(rightInorder, rightPostorder))
