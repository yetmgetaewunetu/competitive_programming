from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        keysl = list(count.keys())
        
        for k in keysl:
           
            if count[k] > len(nums)//2:
                return k