# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ma = sum(accounts[0])
        for i in accounts:
            tem = sum(i)
            if tem > ma:
                ma = tem
        return ma