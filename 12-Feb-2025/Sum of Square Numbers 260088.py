# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i,j = 0, int(sqrt(c)+1)
        while i <= j:
            if i**2 + j**2 == c:
                return True
            elif i **2 + j **2 < c :
                i += 1
            else:
                j -=1
        return False