# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = -1
        lost = -1
        i = 0

        while i < len(nums):
            pos = nums[i] -1
            
            if nums[i] != i +1:
                if nums[pos] == nums[i]:
                    repeated = nums[i]
                    i += 1
                else:
                    nums[i], nums[pos] = nums[pos], nums[i]
            else:
                 i += 1

        for i in range(len(nums)):
            if nums[i] != i +1:
                lost = i + 1
                break

        return [repeated,lost]