# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack  = []
        path = path.split('/')
        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            elif p=='.':
                continue
            elif p!="":
                stack.append(p)
        
        return "/" +"/".join(stack)