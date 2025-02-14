# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(s)
        print(arr)
        left = 0
        total = 0
        for right in range(len(arr)):
            while arr[left] != "1"and left < right:
                left += 1
            if arr[right] == '0':
                arr[left] , arr[right] = arr[right] , arr[left]
                total += right - left 
                left += 1
        return total
        