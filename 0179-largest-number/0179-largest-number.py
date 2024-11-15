class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        large_num = ""
        for i,e in enumerate(nums):
            nums[i] = str(e)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] < nums[j] + nums[i]:
        #             nums[i],nums[j] = nums[j],nums[i]
        nums = self.mergeSort(nums,0,len(nums) - 1)
        if nums[0] == "0":return "0"
        return "".join(nums)
    def mergeSort(self, nums,left,right):
        if left >= right:
            return [nums[left]]
        mid = (right + left)//2
        left_half = self.mergeSort(nums,left,mid)
        right_half = self.mergeSort(nums,mid+1,right)
        return self.merge(left_half,right_half)
    def merge(self, left,right):
        i,j = 0,0
        nums = []
        while i < len(left) and j < len(right):
            if left[i] + right[j] < right[j] + left[i]:
                nums.append(right[j])
                j += 1
            else:
                nums.append(left[i])
                i+= 1

        nums.extend(left[i:])
        nums.extend(right[j:])
        return nums
      