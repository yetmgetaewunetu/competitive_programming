class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l,r = 0, len(nums) -1
        # for i in range(k):
        #     nums.insert(0,nums.pop())
        # return nums

        #using extra space
        res = nums[:] 
        print(res)
        for i,e in enumerate(nums):
            res[(i+k)%len(nums)] = e
        for i,e in enumerate(res):
            nums[i] = e
        return nums