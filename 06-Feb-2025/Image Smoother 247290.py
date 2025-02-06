# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img) , len(img[0])
        arr = [[0] * m for i in range(n)]
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1), (0, 0), (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
        for i in range(n):
            for j in range(m):
                sum , count = 0 , 0
                for xx, yy in directions:
                    x,y = i + xx , j + yy
                    if 0 <= x < n and 0 <= y < m:
                        sum += img[x][y]
                        count += 1
                arr[i][j] = floor(sum/count)
    
        return arr
        
