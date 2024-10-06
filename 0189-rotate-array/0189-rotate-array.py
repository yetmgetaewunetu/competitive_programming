class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l,r = 0, len(nums) -1
        for i in range(k):
            nums.insert(0,nums.pop())
        return nums