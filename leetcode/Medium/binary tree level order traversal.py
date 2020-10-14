# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = [root]
        ret = []
        while len(q)>0:
            curr = []
            n = len(q)
            for i in range(n):
                tmp = q.pop(0)
                if tmp.left != None:
                    q.append(tmp.left)
                if tmp.right != None:
                    q.append(tmp.right)
                curr.append(tmp.val)
            ret.append(curr)
        return ret
