class Solution:
    def findMin(self, nums: List[int]) -> int:
        position = 0
        while position < len(nums):
            if nums[position]< nums[position -1] and position > 0:
                return nums[position]
            position +=1
        return nums[0]