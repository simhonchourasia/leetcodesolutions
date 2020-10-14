# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.q = [None for i in range(k)]
        self.head = 0
        self.tail = -1
        self.cap = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.tail+=1
        self.tail%=self.cap
        if self.isEmpty():
            self.head=self.tail
        self.q[self.tail]=value
        return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.q[self.head] = None
        if self.q[(self.head+1)%self.cap] == None:
            return True
        self.head = (self.head+1)%self.cap
        return True
        
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.tail]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.q[self.head]==None
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.q[(self.tail+1)%self.cap] != None
