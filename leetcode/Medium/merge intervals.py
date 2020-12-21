# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0]) # Sort by first element of interval
        ret = []
        def helper(intervals, curr):
            if len(intervals) == 0:
                ret.append(curr)
                return
            if intervals[0][0] <= curr[1]:
                curr = [curr[0], max(curr[1], intervals[0][1])]
                helper(intervals[1:], curr)
                return
            ret.append(curr)
            helper(intervals[1:], intervals[0])
        helper(intervals[1:], intervals[0])
        return ret
