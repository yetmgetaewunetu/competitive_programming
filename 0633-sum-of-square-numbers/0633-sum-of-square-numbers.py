class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = list(range(int(math.sqrt(c)) + 1))
        left,right = 0,len(nums) -1
        
        while left <= right:
           
            if (nums[left]**2) + (nums[right] **2) == c:
                return True
            elif (nums[left] ** 2)== c or (nums[right]**2) == c:
                return True
            elif (nums[left]**2) + (nums[right] **2) < c:
                left += 1
            else:
                right -= 1
        return False