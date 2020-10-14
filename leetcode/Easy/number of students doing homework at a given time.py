# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        N = len(startTime)
        # Create difference array
        diff = [0 for i in range(1001)]
        for i in range(N):
            diff[startTime[i]-1] += 1
            diff[endTime[i]] -= 1
        # Create prefix-sum array
        psa = [0 for i in range(1001)]
        for i in range(1000):
            # Convert difference array into actual values
            psa[i+1] = psa[i]+diff[i]
        return psa[queryTime]
    
# Time Complexity: O(N), where N is total time
# We only do one pass through the difference array to put in the proper values
# And another pass through the difference array to create the prefix-sum array
