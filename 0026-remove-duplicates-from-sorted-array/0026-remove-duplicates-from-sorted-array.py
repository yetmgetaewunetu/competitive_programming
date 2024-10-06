class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left, right = 0,1
       
        # size = len(nums)
        # while nums and right < len(nums):
        #     if nums[left] == nums[right]:
        #         while right < len(nums) and nums[right] == nums[left]:
        #             nums.pop(right)
        #             size -= 1
        #     else:
                
        #         left += 1
        #         right += 1
        # return size
        size = len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                size -= 1
            else:
                i += 1
        return size