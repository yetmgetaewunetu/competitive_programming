# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {0:1}
        total = 0
        res = 0
        for num in nums:
            total += num
            if total - k in memo:
                res += memo[total-k]
            memo[total] = memo.get(total,0) + 1
        return res
        
        
        
        
        
        
        
        
        
        # prefix = [nums[0]]
        # for i in range(1,len(nums)):
        #     prefix.append(prefix[-1] + nums[i])
        # res = 0
        # for r in range(len(prefix)):
        #     i = 0
        #     if prefix[r] == k:
        #         res += 1
        #     while i < r:
        #         if prefix[r] - prefix[i] == k:
        #             res += 1
        #         i += 1
        # return res