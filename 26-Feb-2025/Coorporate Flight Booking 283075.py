# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n)
        for i in bookings:
            l,r,s = i
            prefix[l-1] += s
            if r < n:
                prefix[r] -= s
        sum = 0
       
        res = []
        for i in prefix:
            sum += i
            res.append(sum)

        return res
        
        