# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque([0])
        

        while q:
            key = q.popleft()
            visited.add(key)
            
            for k in rooms[key]:
                if k not in visited:
                    q.append(k)

        return len(visited) == len(rooms)
