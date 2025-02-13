# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        l = res = 0
        for r in range(len(fruits)):
            window[fruits[r]] = window.get(fruits[r],0) + 1
            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
            res = max(res, r -l+1)
        return res