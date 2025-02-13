# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        window = Counter()
        i,j = 0, float('inf') 
        flag = True
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            while t - window == {}:
                flag = False
                
                if r-l+1 < j-i+1:
                    i,j = l,r
                window[s[l]] -=1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        if j == float('inf'):
            return ""
        else:
            return s[i:j+1]