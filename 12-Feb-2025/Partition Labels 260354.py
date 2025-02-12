# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        dicc = {}
        for i,ch in enumerate(s):
            dicc[ch] = i
        l , r = 0 , 0
        for i,ch in enumerate(s):
            r = max(r,dicc[ch])
            if i == r:
                result.append(i-l+ 1)
                l = i+1
        return result
            

        