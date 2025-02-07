# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        re = []
        cou = Counter(nums)
        for c in cou:
            if cou[c] > k:
                re.append(c)
        return re