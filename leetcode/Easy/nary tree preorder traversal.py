# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Solution:
    
    def preorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        tmp = []
        for node in root.children:
            tmp += self.preorder(node)
        return [root.val] + tmp
