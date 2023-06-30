class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        numm = []
        for i in num:
            numm.insert(0, i)
        nums = ''
        for i in numm:
            nums += i 
        if '-' in nums:
            return False
        else:
            if int(nums) == x:
                return True
            else:
                return False
