# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (len(s) + 1)
        for i in shifts:
            start = i[0]
            end = i[1]
            dirr = i [2]

            if dirr == 0:
                arr[start] -= 1
                if end + 1 < n:
                    arr[end+1] += 1

            else:
                arr[start] += 1
                if end+1 < n:
                    arr[end+1] -= 1
        print(arr)
        cum_arr = []
        sum = 0
        for i in range(n):
            sum += arr[i]
            cum_arr.append(sum)
        ss = ""

        for i in range(n):
            ch = ord(s[i]) - ord('a')
            ch = ch + cum_arr[i]
            gg = chr((ch % 26) + ord('a'))
            ss += gg

            
            
        return ss