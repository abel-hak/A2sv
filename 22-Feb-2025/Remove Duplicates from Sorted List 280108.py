# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        pre = head
        if pre is None:
            return head
        
        while pre and pre.next:
            current = pre.next
            if current.val == pre.val:
                pre.next = current.next
            else:
                pre = pre.next
        
        return head
