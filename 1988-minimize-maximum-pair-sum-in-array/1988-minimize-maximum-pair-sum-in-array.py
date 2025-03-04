class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        r = len(nums)//2
        l  = r-1
        while l >= 0:
            res = max(res,nums[l] + nums[r])
            l -=1
            r+=1
        return res