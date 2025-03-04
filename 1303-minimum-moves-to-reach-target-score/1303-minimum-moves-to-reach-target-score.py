class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if target%2 and maxDoubles:
                target -=1
                res +=1
            elif maxDoubles and target%2 ==0:
                target //=2
                res +=1
                maxDoubles -=1
            elif not maxDoubles:
                res += target -1
                return res
        return res
