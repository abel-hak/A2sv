# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count +=  1
            current = current.next
        if count % 2 == 0:
            count = count // 2
            count += 1
            current = head
            for _ in range(count-1):
                current = current.next
            return current
        else:
            count = count // 2
            current = head
            for _ in range(count):
                current = current.next
            return current
            

        