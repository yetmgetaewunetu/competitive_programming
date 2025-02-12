# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j, res = 0 , len(height)-1, 0
        while i < j:
            res = max(res, (j-i)*min(height[j], height[i]))
            if height[i] < height[j]:
                i += 1
            else:
                j -=1
        return res