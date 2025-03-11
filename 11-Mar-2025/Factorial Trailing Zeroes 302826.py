# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    # def factorial(self,n):
    #     if n <= 1:
    #         return 1
    #     return n * self.factorial(n-1)

    def trailingZeroes(self, n: int) -> int:
        if n <5:
            return 0

        return n//5 + self.trailingZeroes(n//5)





        # fact = self.factorial(n)
        # zeros = 0
        # while fact % 10 == 0:
        #     zeros += 1
        #     fact //= 10
        # return zeros