# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tot = 0
        for i in range(len(nums)):
            nums[i] += tot
            tot = nums[i]
        return nums