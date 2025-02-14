# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        cur = 0
        for j in range(1,len(nums)-1):
            cur = nums[j]
            l,r = 0, len(nums)-1
            while l < j < r:
                temp = nums[l] + nums[r]
                if abs(target - (cur + temp )) < abs(target-closest):
                    closest = cur + temp
                if temp + cur < target:
                    l += 1
                elif temp + cur > target:
                    r -=1
                else:
                    return temp + cur
        return closest