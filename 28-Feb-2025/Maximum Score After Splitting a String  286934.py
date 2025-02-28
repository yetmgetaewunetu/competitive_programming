# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        forward = []
        back = [0]*len(s)
        cur = res = 0
        for i in range(len(s)):
            if s[i] == '0':
                cur += 1
                forward.append(cur)
            else:
                forward.append(cur)
        cur = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                cur += 1
                back[i] = cur
            else:
                back[i] = cur
        for i in range(len(forward)-1):
            res = max(res, forward[i]+back[i+1])

        return res
        