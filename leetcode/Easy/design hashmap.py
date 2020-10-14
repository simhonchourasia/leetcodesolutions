# https://leetcode.com/problems/design-hashmap/

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [[] for i in range(10000)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        b = key % 10000
        # Put keys and values into buckets
        for kv in self.buckets[b]:
            if kv[0]==key:
                kv[1] = value
                return
        self.buckets[b].append([key, value])
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        b = key % 10000
        # Buckets are for easy access
        for kv in self.buckets[b]:
            if kv[0] == key:
                return kv[1]
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        b = key % 10000
        for kv in self.buckets[b]:
            if kv[0] == key:
                self.buckets[b].remove(kv)
        
# Worst case: O(sqrt(N)) access, where N is the range
