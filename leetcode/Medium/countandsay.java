// https://leetcode.com/problems/count-and-say/

class Solution {
    public String countAndSay(int n) {
        // base case
        if (n == 1) return "1";

        String lastcase = countAndSay(n-1); // recursively call the previous case
        String ret = "";
        // general case
        for (int i = 0; i < lastcase.length(); i++) {
            for (int j = i; j < lastcase.length(); j++) {
                // look for how many times a number appears
                // add the number of times a number appears and the number itself to ret
                if ((lastcase.charAt(i) != lastcase.charAt(j))) {
                    ret += Integer.toString(j - i);
                    ret += lastcase.charAt(i);
                    i = j; j--;
                }
                else if (j == lastcase.length() - 1) {
                    ret += Integer.toString(j - i + 1);
                    ret += lastcase.charAt(i);
                    i = j;
                }
            }
        }
        return ret;
    }
}