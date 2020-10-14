# https://leetcode.com/problems/insertion-sort-list/

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        prev = head
        node1 = head.next
        while node1 != None:
            if node1.val>=prev.val:
                prev=node1
                node1 = node1.next
            else:
                tmp = head
                prevtmp = head
                prev.next = node1.next
                while node1.val>tmp.val:
                    prevtmp=tmp
                    tmp=tmp.next
                if tmp==head:
                    head=node1
                else:
                    prevtmp.next=node1
                node1.next=tmp
                node1=prev.next
                
        return head
