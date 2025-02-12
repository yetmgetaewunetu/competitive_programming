# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k <= 0:
            return nums
        nums.reverse()
        n = len(nums)
        i,j = 0,(k-1)%n
        while i <=j:
            nums[i],nums[j] = nums[j],nums[i]
            i,j = i+1,j-1
        if k != n:
            i,j = k%n,n-1
            while i <= j:
                nums[i],nums[j] = nums[j],nums[i]
                i,j = i+1,j-1
            