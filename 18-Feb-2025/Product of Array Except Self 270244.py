# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        pro = 1
        for num in nums:
            if num == 0:
                zeros += 1
                if zeros == 2:
                    return [0] * len(nums)
            else:
                pro *= num
        
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = pro
            return nums
        for i in range(len(nums)):
            nums[i] = pro // nums[i]
        return nums
