# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max1 = max(costs) + 1
        arr = [0] * max1
        for i in costs:
            arr[i] += 1
        index = 0
        for i in range(len(arr)):
            value = arr[i]
            while value > 0:
                costs[index] = i
                index += 1
                value -=1
        count = 0
        for i in costs:
            if i <= coins:
                coins -= i
                count += 1
        return count

