class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        N = []
        for i, t in enumerate(nums):
            N.append([t, i])
        N.sort()
        res = []
        for i in range(len(N)):
            
            if N[i][0] == target:
                res.append(i)
            if N[i][0] > target: break
        res.sort()
        return res