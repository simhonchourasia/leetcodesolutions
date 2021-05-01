// https://leetcode.com/problems/jump-game-ii/

class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 0; // base case
        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1000000; // arbitrarily large number that can never be reached
        }
        // general DP case
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 1; j <= nums[i]; j++) {
                if (i + j >= nums.length) {
                    break;
                }
                else {
                    dp[i+j] = Math.min(dp[i+j], 1 + dp[i]);
                }
            }
        }
        return dp[dp.length - 1];
    }
}