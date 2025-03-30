# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def isPossible(lowest,limit):
            baskets = 0
            target = lowest
            cur_sum = 0

            for pos in position:

                if pos >= target:
                    baskets += 1
                    target = pos + limit

            return baskets >= m
                    

        res = 0
        low,high = 0,max(position)

        while low <= high:
            mid = (low + high) // 2


            if isPossible(position[0],mid):
                res = mid
                low = mid + 1
            else:
                high = mid -1
        return res