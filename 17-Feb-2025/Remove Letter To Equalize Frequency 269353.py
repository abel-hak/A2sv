# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word) 
        for i in range(len(word)):  
            temp_word = word[:i] + word[i+1:]  
            temp_freq = Counter(temp_word)  
            if len(set(temp_freq.values())) == 1:  
                return True
        
        return False