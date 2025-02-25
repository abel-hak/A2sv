# Problem: Longest Mountain in Array - https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        max_length = 0
        n = len(arr)

        for i in range(1, n - 1):
            # Check if it's a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1
                
                # Expand left
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                
                # Expand right
                while right < n - 1 and arr[right + 1] < arr[right]:
                    right += 1
                
                # Calculate length
                mountain_length = right - left + 1
                max_length = max(max_length, mountain_length)

        return max_length
                