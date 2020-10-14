# https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.S = [];
        self.mn = 1000000000000;

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.S.append(x);
        if (x < self.mn):
            self.mn = x;
        

    def pop(self):
        """
        :rtype: None
        """
        t = self.S.pop(len(self.S)-1);
        try:
            self.mn = min(self.S);
        except:
            self.mn = 1000000000000;

    def top(self):
        """
        :rtype: int
        """
        return self.S[-1];
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.S);
        
