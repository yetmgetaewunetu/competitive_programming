class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = dict()
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in losers:
                losers[winner] = 0
            if loser not in losers:
                losers[loser] = 1
            elif loser in losers:
                losers[loser] += 1
        print(losers)
        res = [[],[]]
        for key,value in losers.items():
            if value == 0:
                res[0].append(key)
            elif value == 1:
                res[1].append(key)
        res[0].sort()
        res[1].sort()
        return res