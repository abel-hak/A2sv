# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n5 = 0
        n10 = 0
        n20 = 0
        for i in bills:
            if i == 5:
                n5 += 1
            elif i == 10:
                if n5 > 0:
                    n10 += 1
                    n5 -= 1
                else:
                    return False
            elif i == 20:
                if n5 > 0 and n10 > 0:
                    n5-=1
                    n10-=1
                    n20+=1
                elif n5 > 2:
                    n5-=3
                    n20 += 1
                else:
                    return False
        return True