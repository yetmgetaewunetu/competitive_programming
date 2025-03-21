# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(visited):
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for i in range(len(nums)):
                if i not in visited:
                    cur.append(nums[i])
                    visited.add(i)
                    backtrack(visited)
                    visited.remove(i)
                    cur.pop()
        backtrack(set())
        return res