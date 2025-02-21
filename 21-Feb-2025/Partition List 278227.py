# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next

        res = []
        dicc = defaultdict(int)
        for i in range(len(arr)):
            if arr[i] < x:
                dicc[arr[i]]+=1
        for i in range(len(arr)):
            if arr[i] in dicc:
                res.append(arr[i])
        for i in range(len(arr)):
            if arr[i] not in dicc:
                res.append(arr[i])
        
        current = head
        for i in range(len(res)):
            current.val = res[i]
            current = current.next
        return head        