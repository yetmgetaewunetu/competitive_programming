# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res  = 0
        for i in range(len(nums)-1,1,-1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return res