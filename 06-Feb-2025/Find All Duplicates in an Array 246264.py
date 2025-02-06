# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cou = Counter(nums)
        re = []
        for val in cou:
            if cou[val] == 2:
                re.append(val)
        return re