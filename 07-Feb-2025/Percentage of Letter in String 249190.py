# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cou = 0
        for i in s:
            print(i,letter)
            if i == letter:
                cou += 1
        print(cou)
        return int((cou / len(s)) * 100 )