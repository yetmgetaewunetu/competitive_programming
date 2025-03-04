# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        newCost = sorted(costs,key=lambda cost:abs(cost[1]-cost[0]),reverse=True)
        res = 0
        a,b = 0,0
        
        for cost in newCost:
            if cost[0] <= cost[1]:
                if a <len(costs)//2:
                    res += cost[0]
                    a+=1
                else:
                    res += cost[1]
                    b+=1
            else:
                if b < len(costs)//2:
                    res += cost[1]
                    b +=1
                else:
                    res += cost[0]
                    a +=1
        return res