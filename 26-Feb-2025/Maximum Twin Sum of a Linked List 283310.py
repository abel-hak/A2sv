# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        current = head
        
        # Step 1: Store values in an array
        while current:
            values.append(current.val)
            current = current.next
        
        # Step 2: Compute twin sums using indices
        max_twin_sum = 0
        n = len(values)
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_twin_sum = max(max_twin_sum, twin_sum)
        
        return max_twin_sum
