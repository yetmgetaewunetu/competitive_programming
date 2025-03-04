# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        l,r = 0,0
        # print(points)
        for point in points:
            if l == r ==0:
                res += 1
                l ,r = point
            elif point[0] <= r:
                l = max(l,point[0])
                r = min(r,point[1])
            elif point[1] > r:
                res +=1
                l,r = point
            # print(l,r,res)
        return res
