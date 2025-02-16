# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            sorted_array = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1

            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])
            return sorted_array

        return merge_sort(nums)
