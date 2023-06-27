class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numss = set(nums)
        for num in numss:
            if nums.count(num) > len(nums)//2:
                return num
            