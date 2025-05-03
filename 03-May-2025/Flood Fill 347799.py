# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        queue = deque([(sr,sc)])
        image[sr][sc] = color
        options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        while queue:
            r, c = queue.popleft()

            for x, y in options:
                new_x = r + x
                new_y = c + y

                if 0 <= new_x < m and 0 <= new_y < n and image[new_x][new_y] == original:
                    if (new_x, new_y) in visited:
                        continue

                    queue.append((new_x,new_y))
                    image[new_x][new_y] = color
            
            visited.add((r,c))
            image[r][c] = color

        return image