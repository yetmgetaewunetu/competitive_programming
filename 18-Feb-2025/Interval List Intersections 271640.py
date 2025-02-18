# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i=j = 0
        while i < len(firstList) and j < len(secondList):
            a1,b1 = firstList[i]
            a2,b2 = secondList[j]
            if a1<=b2 and a2 <= b1:
                res.append([max(a1,a2), min(b1,b2)])
            if b2 > b1:
                i += 1
            else:
                j += 1
        return res

