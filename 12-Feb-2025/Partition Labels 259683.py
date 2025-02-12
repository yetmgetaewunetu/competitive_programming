# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexes = {e:i for i, e in enumerate(s)}
        res = []
        i,j = 0,0
        while i < len(s) and j < len(s):
            temp = indexes[s[i]]
            while j < temp:
                if indexes[s[j]] > temp:
                    temp = indexes[s[j]]
                j += 1
            res.append(j+1-i)
            i = j+1
        return res
