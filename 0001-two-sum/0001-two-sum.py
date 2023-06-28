class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lo , hi= 0, len(nums)-1
        lis = []
        for i in range(len(nums)):
            lis.append([nums[i], i])
        lis.sort()
        while lo < hi:
            if lis[lo][0] + lis[hi][0] == target:
                return [lis[lo][1], lis[hi][1]]
            elif lis[lo][0] + lis[hi][0] < target:
                lo += 1
            else:
                hi -= 1
        