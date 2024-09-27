class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = set(range(left,right+ 1))
        for items in ranges:
            if items[0] > right:
                continue
            if items[1] < left:
                continue
            
            for num in range(items[0], items[1] + 1):
                if num in nums: nums.remove(num)
        return len(nums) == 0