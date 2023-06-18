class Solution:
    def findMin(self, nums: List[int]) -> int:
        list1= sorted(nums)
        mini = list1[0]
        return mini
        # lo , hi= 0, len(nums)-1
        # if nums[0]== mini:
        #     return 
        # while lo < hi:
        #     mid  = (lo + hi)// 2
        #     if nums[mid]