// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    public String longestPalindrome(String s) {
        boolean[][] dp = new boolean[s.length()][s.length()];
        // dp[i][i] = true for i = 0, 1, ..., n-1, where n is length of string
        for (int i = 0; i < s.length(); i++) {
            dp[i][i] = true;
        }
        // general case
        for (int j = 0; j < s.length(); j++) {
            for (int i = j - 1; i >= 0; i--) {
                if (j - i == 1) {
                    dp[i][j] = (s.charAt(i) == s.charAt(j));
                }
                else {
                    dp[i][j] = dp[i+1][j-1] && (s.charAt(i) == s.charAt(j));
                }
            }
        }

        // get max
        int mx = -1;
        int a = -1; int b = -1;
        for (int j = 0; j < s.length(); j++) {
            for (int i = j; i >= 0; i--) {
                if (dp[i][j] && j - i > mx) {
                    mx = j - i;
                    a = i; b = j;
                }
            }
        }

        return s.substring(a, b+1);
    }
}