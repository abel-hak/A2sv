# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dd = Counter(chars)
        sum = 0
        for i in words:
            b = Counter(i)
            cou = 0
            for j in i:
                if b[j] <= dd[j]:
                    cou += 1
            if cou == len(i):
                sum += cou
        return sum