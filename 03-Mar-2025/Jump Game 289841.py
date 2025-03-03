# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        k = 1
        while i < len(nums):
            if i + nums[i] >= len(nums)-1:
                return True
            if nums[i] == 0 and i != len(nums) -1:
                return False
            num = i + nums[i]
            good = num
            for j in range(k, i + nums[i] + 1):
                if j + nums[j] >=len(nums)-1:
                    return True
                if j + nums[j] > good:
                    good = max(good,j + nums[j])
                    i = j
                k = j
            if good == num:
                i += 1
            
        return False