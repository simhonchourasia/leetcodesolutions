# https://leetcode.com/problems/sort-list/

class Solution:
    
    def sortList(self, head: ListNode) -> ListNode:

        # Implementation of insertion sort with linked lists
        def insert(head, val):
            if head == None:
                return ListNode(val = val, next = None)
            if val <= head.val:
                return ListNode(val = val, next = head)
            return ListNode(val = head.val, next = insert(head.next, val))
        
        def inserthelper(head, acc):
            if head == None:
                return acc
            return inserthelper(head.next, insert(acc, head.val))
        #return inserthelper(head, None)
        
        # Implementation of merge sort with linked lists

        # Break up the linked list into smaller linked lists, each containing one element
        def breakup(head):
            ret = []
            h = head
            while h != None:
                ret.append(ListNode(val = h.val, next = None))
                h = h.next
            return ret

        # Helper function to merge two sorted linked lists
        def merge(head1, head2):
            if head1 == None:
                return head2
            if head2 == None:
                return head1
            if head1.val <= head2.val:
                return ListNode(val = head1.val, next = merge(head1.next, head2))
            if head2.val <= head1.val:
                return ListNode(val = head2.val, next = merge(head1, head2.next))

        # Keeps two lists, with the invariant that every list in the two lists is sorted
        # Recursively merges lists together until only one remains
        def mergehelper(acc1, acc2):
            if len(acc1) == 0:
                return mergehelper(acc2, [])
            if len(acc1) == 1 and len(acc2) == 0:
                return acc1[0]
            if len(acc1) == 1:
                return mergehelper([], acc1 + acc2)
            return mergehelper(acc1[2:], [merge(acc1[0], acc1[1])] + acc2)
        
        if head == None:
            return None
        #return mergehelper(breakup(head), [])

        # Using standard Python sort
        h = head
        lst = []
        while h != None:
            lst.append(h.val)
            h = h.next
        lst = reversed(sorted(lst))
        ret = None
        for x in lst:
            ret = ListNode(val = x, next = ret)
        return ret
