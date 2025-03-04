# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        win = {"L":0,"R":0}
        for r in range(len(s)):
            win[s[r]] +=1
            if win["L"] == win["R"]:
                res +=1
                win["L"] = win["R"] = 0
        return res