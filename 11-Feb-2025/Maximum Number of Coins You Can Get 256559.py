# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        j = len(piles) - 2
        sum = 0
        for i in range((len(piles) // 3)):
            sum += piles[j]
            j -= 2


            
        return sum

        