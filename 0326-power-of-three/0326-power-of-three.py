class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n = n / 3
        if n == 1.0:
            return True
        else:
            return False