class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0,1
       
        size = len(nums)
        while nums and right < len(nums):
            if nums[left] == nums[right]:
                while right < len(nums) and nums[right] == nums[left]:
                    nums.pop(right)
                    size -= 1
            else:
                
                left += 1
                right += 1
        return size