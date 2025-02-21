# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Copy the original linked list (so we don't modify it)
        temp = head
        copy_head = self.cloneList(head)
        
        # Step 2: Reverse the cloned linked list
        new_head = self.reverseList(copy_head)

        # Step 3: Compare both lists
        while temp and new_head:
            if temp.val != new_head.val:
                return False
            temp = temp.next
            new_head = new_head.next

        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
    
    def cloneList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0)
        current_new = dummy
        current_old = head

        while current_old:
            current_new.next = ListNode(current_old.val)
            current_new = current_new.next
            current_old = current_old.next

        return dummy.next
