# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validateMid(capacity):
            cur_sum = 0
            days_cnt = 1
            for w in weights:
                cur_sum += w
                if cur_sum > capacity:
                    days_cnt += 1
                    cur_sum = w
                if days_cnt > days:
                    return False
            return True
            
            # i = 0
            # for j in range(days):
            #     if i == len(weights):
            #         return True
            #     cur = 0
            #     while cur <= capacity and i < len(weights):
            #         cur += weights[i]
            #         if cur <= capacity:
            #             i += 1
            
            # return i == len(weights)


        low = max(weights)
        high = sum(weights)
        answer = 0
        while low <= high:
            mid = (low + high)//2
            if validateMid(mid):
                answer = mid
                high = mid -1
            else:
                low = mid + 1

        return answer
    
                


