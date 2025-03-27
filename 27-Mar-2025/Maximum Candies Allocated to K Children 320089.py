# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canGive(amount):
            if amount == 0:
                return True
            childs = 0
            for candy in candies:
                childs += candy // amount
            return childs >= k


        low ,right = 0,max(candies)
        ans = low
        while low <= right:
            mid = (low + right)//2
            if canGive(mid):
                ans = mid
                low = mid + 1
            else:
                right = mid -1
        return ans