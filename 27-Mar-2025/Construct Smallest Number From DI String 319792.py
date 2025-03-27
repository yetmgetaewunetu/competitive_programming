# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = None
        path = []
        def backtrack(ind):
            nonlocal res,path
            if len(path) == len(pattern) + 1:
                res = [str(i) for i in path]
                res = ''.join(res)
                return
            if ind == -1:
                for i in range(1,10):
                    path.append(i)
                    backtrack(ind+1)
                    path.pop()
            else:
                if pattern[ind] == 'I':
                    for i in range(1, 10):
                        if res:
                            return
                        if i not in path and i > path[-1]:
                            path.append(i)
                            backtrack(ind + 1)
                            path.pop()
                else:
                    for i in range(1,10):
                        if res:
                            return
                        if i not in path and i < path[-1]:
                            path.append(i)
                            backtrack(ind + 1)
                            path.pop()
        backtrack(-1)
        return res


        
        
        
        
        
        
        
        
        
        
        
        # res = None
        # path = []
        # def backtrack():
        #     nonlocal res,path
        #     if len(path) == len(pattern) +1:
        #         for i in range(len(pattern)):
        #             if pattern[i] == 'I' and path[i+1] < path[i]:
        #                 return 
        #             if pattern[i] == 'D' and path[i+1] > path[i]:
        #                 return
        #         if not res:
        #             res = [str(i) for i in path]
        #             res = "".join(res)
        #             return
                        
        #     for i in range(1,10):
        #         if res:
        #             return
        #         if i not in path:
        #             path.append(i)
        #             backtrack()
        #             path.pop()
        # backtrack()
        # return res
        
