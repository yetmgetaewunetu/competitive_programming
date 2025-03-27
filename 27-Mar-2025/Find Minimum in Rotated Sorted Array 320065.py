# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,right = 0,len(nums)-1
        res = nums[-1]
        while low <= right:
            mid = (low + right) //2
            if nums[mid] <= nums[right]:
                res = min(nums[mid], res)
                right = mid -1
            elif nums[mid] > nums[right]:
                low = mid + 1
        return res