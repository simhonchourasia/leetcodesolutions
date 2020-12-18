# https://leetcode.com/problems/summary-ranges/submissions/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        for i in range(len(nums)-1, 0, -1):
            if nums[i] - nums[0] == i:
                return [str(nums[0]) + "->" + str(nums[i])] + self.summaryRanges(nums[i+1:])
        return [str(nums[0])] + self.summaryRanges(nums[1:])
