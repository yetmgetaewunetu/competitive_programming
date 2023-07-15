class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        
        if max(nums) < length:
            return length
        elif 0 not in nums:
            return 0
        else:
            for i in range(1, length):
                if nums[i] - nums[i - 1] == 2:
                    return  nums[i - 1] + 1

