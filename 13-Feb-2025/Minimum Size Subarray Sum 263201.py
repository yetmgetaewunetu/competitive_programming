# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = left = 0
        res = len(nums)+1
        for right in range(len(nums)):
            window += nums[right]
            while window >= target:
                res = min(res, right-left+1)
                window -= nums[left]
                left += 1
        if res == len(nums) +1:
            return 0
        return res