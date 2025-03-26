# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def backtrack(cur):
            if cur ==0:
                res.append("".join(path[:]))
                return
            openning = path.count('(')
            closing = path.count(')')
            if openning >= closing:
                if openning < n:
                    path.append('(')
                    backtrack(cur-1)
                    path.pop()
                path.append(')')
                backtrack(cur-1)
                path.pop()
        backtrack(2*n)
        return res