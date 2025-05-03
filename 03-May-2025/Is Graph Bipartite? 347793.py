# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        result = True

        def dfs(row):
            temp = True

            for nei in graph[row]:
                if color[nei] == -1:
                    if color[row] == 0:
                        color[nei] = 1
                    else:
                        color[nei] = 0
                    temp = temp and dfs(nei)

                elif color[nei] == color[row]:
                    return False

            return temp
        
        for row in range(len(graph)):
            if color[row] == -1:
                color[row] = 0
                result = result and dfs(row)

        return result
            