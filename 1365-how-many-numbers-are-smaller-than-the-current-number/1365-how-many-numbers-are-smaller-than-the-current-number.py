class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            y = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j !=i:
                    y +=1
                   
            x.append(y)
        return x