# https://leetcode.com/problems/path-sum-ii/

class Solution:
        def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
            ret = [] # contains final paths

            # Helper function that recursively calls itself on left and right subtrees
            # Checks if it is a leaf and adds itself to the list of final paths if it is
            def helper(node, currPath):
            if node == None:
                return
            elif node.left == None and node.right == None:
                currPath.append(node.val)
            if sum(currPath) == targetSum:
                ret.append(currPath)
            else:
                helper(node.left, currPath + [node.val])
                helper(node.right, currPath + [node.val])

        # Call with initial empty list accumulator
        helper(root, [])
        return ret