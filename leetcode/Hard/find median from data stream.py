# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        # running median
        self.median = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)
        self.nums = sorted(self.nums)
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        # Update median based on whether there are an even or odd number of elements in the list
        if len(self.nums)%2==1:
            self.median = self.nums[len(self.nums)//2]
        else:
            self.median = (self.nums[len(self.nums)//2]+self.nums[len(self.nums)//2-1])/2.0
        return self.median
        
