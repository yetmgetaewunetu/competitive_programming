# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def power(self,x,n):
        if n==1:return x
        num = self.power(x,n//2)
        if n%2:
            return num * num * x
        return num * num
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        num = self.power(x,abs(n))
        if n < 0:
            return 1/num
        return num
        