# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = 0
        for i in range(len(s)-1):
            if romanDict[s[i]] < romanDict[s[i+1]]:
                ret -= romanDict[s[i]]
            else:
                ret += romanDict[s[i]]
        ret += romanDict[s[-1]]
        return ret
