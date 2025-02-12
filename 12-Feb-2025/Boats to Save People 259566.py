# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j,res  = 0,len(people) -1,0
        while i <= j:
            if people[i] + people[j] > limit:
                j -=1
            else:
                i,j = i+1,j -1
            res += 1
        return res