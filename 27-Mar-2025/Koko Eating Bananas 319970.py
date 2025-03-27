# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatIn(amount):
            hours = 0
            for pile in piles:
                if amount >= pile:
                    hours += 1
                else:
                    hours += math.ceil(pile / amount)
            return hours <= h
        
        high = sum(piles)
        low = math.ceil(sum(piles)/h)
        ans = low

        while low <= high:
            mid = (low + high) //2
            if canEatIn(mid):
                ans = mid
                high = mid -1
            else:
                low = mid +1
        return ans
