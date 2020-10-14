# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.cs = [];
        self.ms = maxSize;
        self.length = 0;
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (self.length < self.ms):
            self.cs.append(x);
            self.length += 1;
        
        

    def pop(self):
        """
        :rtype: int
        """
        if (self.length == 0):
            return -1;
        self.length -= 1;
        return self.cs.pop(self.length);
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, self.length)):
            self.cs[i] += val;
                
        
