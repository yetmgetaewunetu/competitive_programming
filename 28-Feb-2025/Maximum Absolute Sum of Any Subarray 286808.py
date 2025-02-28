# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        nums =  nums
        max_pos = 0
        min_neg = 0
        for num in nums:
            res = max(res, abs(num -max_pos), abs(num-min_neg))
            if num > 0:
                max_pos = max(max_pos, num)
            elif num <0:
                min_neg = min(min_neg,num)
        return res