// https://leetcode.com/problems/partition-list/

class Solution {
    // Helper function to reverse a linked list
    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        ListNode nxt = null;
        while (curr != null) {
            nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    }
            
    
    // First add the nodes less than x
    // Then add the nodes greater than x
    // Desired list is created in reverse order
    // So at the end, reverse the linked list
    public ListNode partition(ListNode head, int x) {
        ListNode ret = null;
        ListNode tmp = head;
        while (tmp != null) {
            if (tmp.val < x) {
                ret = new ListNode(tmp.val, ret); 
            }
            tmp = tmp.next;
        }
        tmp = head;
        while (tmp != null) {
            if (tmp.val >= x) {
                ret = new ListNode(tmp.val, ret);
            }
            tmp = tmp.next;
        }
        
        
        return reverseList(ret);
    }
}
