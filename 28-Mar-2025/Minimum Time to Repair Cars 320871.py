# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isValid(limit):
            cur = 1
            cars_taken = 0

            for rank in ranks:
                temp = limit // rank
                cur_cars= math.floor(math.sqrt(temp))
                cars_taken += cur_cars
                new_time = cur_cars * rank * rank
                cur = max(cur,new_time)

                if cars_taken >= cars:
                    return cur
            return False

        min_num = min(ranks)
        low,high = 1, min_num * cars * cars
        res = high

        while low <= high:
            mid = (high + low)//2

            if isValid(mid):
                res = mid
                high = mid -1

            else:
                low = mid + 1

        return res