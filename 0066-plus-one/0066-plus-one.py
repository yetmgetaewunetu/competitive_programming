class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return [1]
        else:
            stri = ''
            for num in nums:
                stri += str(num)
            numstring = str(int(stri) + 1)
            List = []
            for i in numstring:
                List.append(int(i))
            return List