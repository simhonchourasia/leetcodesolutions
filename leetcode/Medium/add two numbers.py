# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addHelper(self, l1, l2, carry):
        if l1 == None and l2 == None:
            if carry > 0:
                return ListNode(val=1, next=None)
            return None
        
        if l1 == None:
            if l2.val + carry > 9:
                return ListNode(val = 0, next=self.addHelper(None, l2.next, 1))
            return ListNode(val = l2.val+carry, next=self.addHelper(None, l2.next, 0))
        
        if l2 == None:
            if l1.val + carry > 9:
                return ListNode(val = 0, next=self.addHelper(l1.next, None, 1))
            return ListNode(val = l1.val+carry, next=self.addHelper(l1.next, None, 0))
        
        if l1.val+l2.val+carry > 9:
            return ListNode(val = (l1.val+l2.val+carry)-10, next=self.addHelper(l1.next, l2.next, 1))
        return ListNode(val = (l1.val+l2.val+carry), next=self.addHelper(l1.next, l2.next, 0))
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addHelper(l1, l2, 0)
