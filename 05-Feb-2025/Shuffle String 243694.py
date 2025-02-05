# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(s)
        res = [""] * len(arr)
        for i in range(len(indices)):
            res[indices[i]] = arr[i]
        
        return "".join(res)

        