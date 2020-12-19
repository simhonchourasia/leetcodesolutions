# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        if head.val == head.next.val:
            return self.deleteDuplicates(head.next)
        return ListNode(val=head.val, next=self.deleteDuplicates(head.next))
