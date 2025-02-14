# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

from typing import List

class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        left = 0
        max1 = 0
        fruit_count = {}
        
        for right in range(len(arr)):
            fruit_count[arr[right]] = fruit_count.get(arr[right], 0) + 1
            
            while len(fruit_count) > 2:
                fruit_count[arr[left]] -= 1
                if fruit_count[arr[left]] == 0:
                    del fruit_count[arr[left]]
                left += 1
            
            max1 = max(max1, right - left + 1)

        return max1
