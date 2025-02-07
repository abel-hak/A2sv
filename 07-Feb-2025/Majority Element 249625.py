# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cou = Counter(nums)
        re = cou.most_common(1)
        return re[0][0]