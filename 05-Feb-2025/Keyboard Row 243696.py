# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = sorted("qwertyuiop")
        row2 = sorted("asdfghjkl")
        row3 = sorted("zxcvbnm")
        re = []
        
        for word in words:
            sorted_word = sorted(word.lower())
            if all(char in row1 for char in sorted_word):
                re.append(word)
            elif all(char in row2 for char in sorted_word):
                re.append(word)
            elif all(char in row3 for char in sorted_word):
                re.append(word)
        
        return re
