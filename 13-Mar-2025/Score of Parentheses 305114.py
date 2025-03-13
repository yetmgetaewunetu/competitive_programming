# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        stack  = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                if not stack:
                    stack.append(i)
                else:
                    temp = i
                    while i < len(s) and stack:
                        if s[i] == '(':
                            stack.append('(')
                        else:
                            stack.pop()
                        i += 1
                    i -=1
                    res += 2 *self.scoreOfParentheses(s[temp:i])
            else:
                if stack:
                    stack.pop()
                    res += 1
            i += 1
        return res

