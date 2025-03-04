# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        for i in s:
            if i == '1':
                ones += 1
        res = ['1' for i in range(ones-1)]
        for j in range(ones,len(s)):
            res.append('0')
        res.append('1')
        return "".join(res)