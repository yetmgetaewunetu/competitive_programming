# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        memo = {0:1}
        res = 0
        for num in nums:
            total += num
            # print(total,memo)
            if total % k in memo:
                res += memo[total%k]
            memo[total%k] = memo.get(total%k,0) + 1
        return res