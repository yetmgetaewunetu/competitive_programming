class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ =  sum(nums[:k])
        cur = summ
        maxi =summ /k 
        i  = 0
        for i in range(1, len(nums) - k  + 1):
            total = cur - nums[i - 1] + nums[i + k - 1 ]
            cur = total
            average = total / k
            maxi = max(maxi, average)
            
        return maxi