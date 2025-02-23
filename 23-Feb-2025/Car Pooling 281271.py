# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        
        for trip in trips:
            num_passengers, start, end = trip
            events.append((start, num_passengers))
            events.append((end, -num_passengers))
        
        events.sort()
        
        current_passengers = 0
        
        for event in events:
            current_passengers += event[1]
            if current_passengers > capacity:
                return False
        
        return True