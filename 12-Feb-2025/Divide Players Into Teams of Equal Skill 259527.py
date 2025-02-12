# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        skill.sort()
        i,j,temp = 0,len(skill) -1, skill[0] + skill[-1]
        while i< j:
            if skill[i] + skill[j] != temp:
                return -1
            res += skill[i] * skill[j]
            i , j= i+1,j -1
        return res