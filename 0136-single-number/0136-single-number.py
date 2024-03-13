class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                del count[num]
            else:
                count[num] = 1
        
        return list(count.keys())[0]