# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        path = []
        def backtrack(cur):
            if cur ==0:
                res.append(''.join(path))
                return
            if not path or (path and path[-1] == '1'):
                path.append('0')
                backtrack(cur-1)
                path.pop()
            
                path.append('1')
                backtrack(cur-1)
                path.pop()
            elif path[-1] == '0':
                path.append('1')
                backtrack(cur -1)
                path.pop()
            
        backtrack(n)
        return res