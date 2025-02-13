# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        window = l = res =0
        
        for r in range(len(s)):
            window += abs(ord(s[r]) - ord(t[r]))
            while window > maxCost:
                window -= abs(ord(s[l])-ord(t[l]))
                l += 1
            res = max(res, r-l+1)
        return res