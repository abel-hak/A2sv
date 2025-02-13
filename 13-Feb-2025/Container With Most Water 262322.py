# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max1 = float('-inf')
        while l < r:
            area = (r-l) * min(height[l],height[r])
            if area > max1:
                max1 = area
            if height[l] < height[r]:
                l+=1
            else:
                r -=1
        return max1
