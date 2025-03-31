# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def checkPossible(radius):
            l = 0
            for heater in heaters:

                while l < len(houses) and heater - radius <= houses[l] <= heater + radius:
                    l += 1
            
            return l == len(houses)
        
        houses.sort()
        heaters.sort()
        
        low,high = 0, max(houses[-1],heaters[-1]) - min(heaters[0],houses[0])
        res = high

        while low <= high:
            mid = (low + high) // 2

            if checkPossible(mid):
                res = mid
                high = mid -1

            else:
                low = mid + 1
        
        return res 