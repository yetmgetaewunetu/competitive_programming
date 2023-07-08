class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            lo , hi = 0 , len(nums) -1
            while lo  < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi =  mid - 1
                
            else:
                
                    if nums[lo] < target:
                        nums.insert(lo + 1, target)
                    else:
                        nums.insert(lo, target)
        return nums.index(target)
                