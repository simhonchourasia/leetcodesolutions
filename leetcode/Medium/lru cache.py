# https://leetcode.com/problems/lru-cache/

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity;
        self.cache = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # O(len(self.cache)) time complexity
        for x in range(len(self.cache)):
            if self.cache[x][0]==key:
                # Put the key-value pair at the end 
                self.cache.append(self.cache.pop(x))
                return self.cache[-1][1]
        return -1
    
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # O((len(self.cache)) time complexity
        for i in range(len(self.cache)):
            # Check if the corresponding key already exists
            if self.cache[i][0] == key:
                self.cache[i][1] = value
                # If it does, put it at the end
                self.cache.append(self.cache.pop(i))
                return
        # Get rid of the least recently used key-value pair if we overcap
        if len(self.cache)==self.cap:
            self.cache.pop(0)
        self.cache.append([key, value])
            
