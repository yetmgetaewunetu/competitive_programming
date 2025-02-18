# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        memo = {0:1}
        current = 0
        for num in nums:
            current += num
            # print(current,memo)
            if current - goal in memo:
                res += memo[current-goal]
            memo[current] = memo.get(current,0) + 1
        return res