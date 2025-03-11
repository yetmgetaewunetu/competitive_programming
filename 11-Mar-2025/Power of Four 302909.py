# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        rep = math.log(n,4)
        if int(rep) == rep:
            return True
        return False