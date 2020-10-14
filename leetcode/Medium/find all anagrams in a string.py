# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        if len(p)>len(s):
            return ret
        # Create a sliding window counter
        og = [0 for i in range(26)]
        counter = [0 for i in range(26)]
        for i in range(len(p)):
            counter[ord(s[i])-97] += 1
            og[ord(p[i])-97] += 1
        if counter == og:
            ret.append(0)
        for i in range(1, len(s)-len(p)+1):
            counter[ord(s[i-1])-97] -= 1
            counter[ord(s[i+len(p)-1])-97] += 1
            #print(str(s[i-1]) + ", " + str(s[i+len(p)-1]))
            if counter == og:
                ret.append(i)
        return ret
