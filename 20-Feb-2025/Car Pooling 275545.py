# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*1002
        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]
            if trip[0]>capacity:
                return False
        # print(prefix)
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
            if prefix[i] >capacity:
                return False
        return True