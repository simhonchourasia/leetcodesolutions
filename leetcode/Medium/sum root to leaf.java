// https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution {
    int ret = 0; // contains the final sum
    
    // Helper function 
    // Recursively calls itself on left and right subtrees
    // Detects if it is at a leaf, and then adds to the final sum
    public void sumHelper(TreeNode root, int acc) {
        if (root == null) return;
        else if (root.left == null && root.right == null) {
            ret += 10 * acc + root.val;
        }
        else {
            acc = acc * 10 + root.val;
            sumHelper(root.left, acc);
            sumHelper(root.right, acc);
        }
    }
    
    // Call helper function and return final sum
    public int sumNumbers(TreeNode root) {
        sumHelper(root, 0);
        return ret;
    }
}
