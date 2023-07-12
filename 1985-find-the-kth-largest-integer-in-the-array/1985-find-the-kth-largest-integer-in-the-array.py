class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_nums = []
        for num in nums:
            int_nums.append(int(num))
        int_nums.sort()
        return str(int_nums[len(nums) - k])