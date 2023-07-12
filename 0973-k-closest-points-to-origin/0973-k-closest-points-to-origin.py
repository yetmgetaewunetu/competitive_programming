import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        List = []
        for i in range(len(points)):
                    List.append([(math.sqrt(points[i][0]**2 + points[i][1]**2)), i])

        List.sort()
        print(List)
        ans = []
        for i in range(k):
            ans.append(points[List[i][1]])
        return ans