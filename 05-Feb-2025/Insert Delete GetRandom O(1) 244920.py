# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet:

    def __init__(self):
        self.data = []  
        self.index_map = {}  

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False  
        self.index_map[val] = len(self.data)  
        self.data.append(val)  
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False  
        

        idx = self.index_map[val]
        

        last_element = self.data[-1]
        self.data[idx] = last_element  
        self.index_map[last_element] = idx  
        
        self.data.pop()
        del self.index_map[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)  

# Example usage:
# obj = RandomizedSet()
# obj.insert(10)
# obj.insert(20)
# obj.remove(10)
# print(obj.getRandom())  # Returns 20 with O(1) complexity
