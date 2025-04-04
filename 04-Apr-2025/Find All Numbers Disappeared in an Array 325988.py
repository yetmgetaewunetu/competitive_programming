# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0

        while i < len(nums):

            correct_pos = nums[i] -1

            if nums[i] == i + 1:
                i += 1
            else:
                if nums[correct_pos] == nums[i]:
                    i += 1
                else:
                    nums[i],nums[correct_pos] = nums[correct_pos],nums[i]
        
        res = []
        for i in range(len(nums)):
            if nums[i] != i +1:
                res.append(i + 1)

        return res