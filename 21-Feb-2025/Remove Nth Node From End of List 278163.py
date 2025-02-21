# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        
        while current:
            current = current.next
            count += 1
        
        if count == n:
            return head.next
        
        current = head
        for _ in range(count - n - 1):
            current = current.next
        
        current.next = current.next.next
        return head
