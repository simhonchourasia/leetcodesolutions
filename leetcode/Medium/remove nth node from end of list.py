# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        k = 0
        # Progress along nodes to reach the end
        while node != None:
            node = node.next
            k += 1
        
        k -= n
        f = ListNode()
        # Delete the node
        f.next = head
        tmp = f
        # Put the rest of the linked list together
        while k > 0:
            k -= 1
            tmp = tmp.next
        tmp.next = tmp.next.next
        return f.next

# Time Complexity: O(sz), where sz is the length of the list, as we go to the end and back
