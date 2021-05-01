// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int mx = 0;
        boolean[] counter = new boolean[256]; // hold ascii 
        for (int i = 0; i < s.length(); i++) {
            // reset ascii counter
            for (int k = 0; k < 256; k++) {
                counter[k] = false;
            }
            // go through substrings starting at index i
            for (int j = i; j < s.length(); j++) {
                int c = s.charAt(j);
                if (counter[c]) {
                    mx = Math.max(mx, j - i);
                    break;
                }
                else if (j == s.length() - 1) { // if it hits the end of the string
                    mx = Math.max(mx, j - i + 1);
                    break;
                }
                else {
                    counter[c] = true; // indicate that the char has been seen already
                }
            }
        }
        return mx;
    }
}