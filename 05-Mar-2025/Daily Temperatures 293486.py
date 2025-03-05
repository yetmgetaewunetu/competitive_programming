# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for r in range(len(temperatures)):
            i = 1
            while stack and temperatures[r] > stack[-1][0]:
                res[stack[-1][1]] = r - stack[-1][1]
                stack.pop()
            stack.append([temperatures[r],r])
        return res