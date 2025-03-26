# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        reserved = set()
        cols = set()
        res = []
        path = []
        def backtrack(row):
            nonlocal reserved,cols,res,path
            if row == n:
                res.append([])
                for r,c in path:
                    temp = ['.' for _ in range(n)]
                    temp[c] = 'Q'
                    res[-1].append("".join(temp))
                return
            for col in range(n):
                reservedd = reserved.copy()
                if (row,col) in reserved or col in cols:
                    continue
                r,c = row,col
                while r<n and c<n:
                    reserved.add((r,c))
                    r += 1
                    c += 1
                r,c = row,col
                while r >=0 and c >= 0:
                    reserved.add((r,c))
                    r -= 1
                    c -=1
                r,c = row,col
                while r>= 0 and c <n:
                    reserved.add((r,c))
                    r -=1
                    c += 1
                r,c = row,col
                while r < n and c >=0:
                    reserved.add((r,c))
                    r += 1
                    c -= 1

                r,c =row, col

                path.append((r,c))
                reserved.add((r,c))
                cols.add(col)

                backtrack(row + 1)
                path.pop()
                reserved.remove((r,c))
                cols.remove(col)

                reserved = reservedd.copy()
        backtrack(0)
        return res

