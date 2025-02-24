# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        res = []
        for num in nums:
            prefix.append(prefix[-1] + num)
        prefix.append(0)
        for i in range(1,len(prefix)-1):
            temp = nums[i-1]*(i-1) - (prefix[i-1]) 
            suff = (prefix[-2] - prefix[i]) - nums[i-1] * (len(nums) - i)
            res.append(temp + suff)
        return res
