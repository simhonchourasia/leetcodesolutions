# https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator:

    def __init__(self, root: TreeNode):
        def inorder(node, acc):
            if node == None:
                return acc
            return inorder(node.left, [node.val] + inorder(node.right, acc))
        self.arr = inorder(root, [])

    def next(self) -> int:
        tmp = self.arr[0]
        self.arr = self.arr[1:]
        return tmp

    def hasNext(self) -> bool:
        return len(self.arr) > 0 and len(self.arr[1:]) >= 0
