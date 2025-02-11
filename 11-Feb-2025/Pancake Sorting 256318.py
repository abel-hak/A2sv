# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        j = len(arr)
        while j > 0:
            max1 = float('-inf')
            k = 0
            for i in range(j):
                if arr[i] > max1:
                    max1 = arr[i]
                    k = i
            if k > 0:
                arr[:k+1] = arr[:k+1][::-1]
                ans.append(k+1)
            print(arr)
            arr[:j] = arr[:j][::-1]
            ans.append(j)

            
            
            j -= 1
       

        return ans

            
        