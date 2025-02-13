# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                window += 1
            while window > k:
                if nums[left] == 0:
                    window -=1
                left += 1
            ans = max(ans, right-left + 1)
        return ans
