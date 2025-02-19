# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 2)
        nums.sort()
        res = 0
        for req in requests:
            prefix[req[0]] += 1
            prefix[req[1]+1] -=1
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        prefix.sort()
        # print(nums,prefix)
        for i in range(-1,-len(nums)-1,-1):
            # print(i)
            res += prefix[i] * nums[i]
        return res %(10**9 + 7)