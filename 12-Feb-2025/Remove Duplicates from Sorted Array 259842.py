# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,0
        while j < len(nums):
            while j <len(nums) and  nums[j] == nums[i]:
                j += 1
            if j < len(nums):
                nums[i+1] = nums[j]
                i +=1
        return i+1