class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        items = set(range(0, len(nums) + 1))
        res = -1
        for num in nums:
            items.remove(num)
        return items.pop()