# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def backtrack(l,r):
            if l >= len(s):
                return

            if len(path) == 3:
                cur = s[l:]
                if int(cur) <= 255 and not (len(cur) > 1 and cur.startswith('0')):
                    path.append(s[l:r])
                    res.append(".".join((path)))
                    path.pop()
                return
            for i in range(l+1,r+1):
                cur = s[l:i]
                if int(cur) > 255 or (len(cur) > 1 and cur.startswith('0')):
                    continue
                path.append(cur)
                backtrack(i,i+3)
                path.pop()
        backtrack(0,3)
        return res