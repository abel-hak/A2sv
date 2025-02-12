# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        sum = 0
        su = skill[0] + skill[n-1]

        for i in range(len(skill) //2):
            if su != skill[i] + skill[n-i-1]:
                return -1
            res = skill[i] * skill[n-i-1]
            
            sum += res
        return sum

        