# https://leetcode.com/problems/design-linked-list/

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedList = [];
        self.length = 0;
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if (index >= 0 and index < self.length):
            return self.linkedList[index];
        return -1;
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.linkedList.insert(0, val);
        self.length += 1;
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.linkedList.append(val);
        self.length += 1;
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if (index >=0):
            if (index < self.length):
                self.linkedList.insert(index, val);
                self.length += 1;
            if (index == self.length):
                self.linkedList.append(val);
                self.length += 1;
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if (index >= 0 and index < self.length):
            self.linkedList.pop(index);
            self.length -= 1;
        
