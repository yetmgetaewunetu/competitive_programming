# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        left,right = 0,len(nums) -1
        res = len(nums)

        while left <= right:

            mid = (left + right) //2

            if nums[mid] != mid:
                right  = mid -1
            else:
                left = mid + 1
        if nums[mid] == mid:
            return mid + 1
        return mid
        
        
        
        
        
        # n = len(nums)
        # sNums = set(nums)
        # for i in range(n +1):
        #     if i not in sNums:
        #         return i
            