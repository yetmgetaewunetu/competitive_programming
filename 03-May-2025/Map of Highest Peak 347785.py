# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = []
        m = len(isWater)
        n = len(isWater[0])

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 0:
                    isWater[i][j] = '#'
                else:
                    isWater[i][j] = 0
                    q.append((i,j))

        for r, c in q:
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nr = r + dx
                nc = c + dy

                if 0 <= nr < m and 0 <= nc < n and isWater[nr][nc] == '#':
                    isWater[nr][nc] = isWater[r][c] + 1
                    q.append((nr, nc))
        
        return isWater