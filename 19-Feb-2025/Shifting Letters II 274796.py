# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 2)
        res = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for l,r,v in shifts:
            if v == 0:
                v = -1
            prefix[l] += v
            prefix[r+1] -= v
        # print(prefix)
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        for i in range( len(s)):
            # print(s.index(s[i]),s[i])
            res.append(alpha[(alpha.index(s[i]) + prefix[i])%26])
        return "".join(res)

        