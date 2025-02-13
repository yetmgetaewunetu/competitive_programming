# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = Counter(s1)
        window = {}
        left = 0
        for right in range(n,len(s2)+1):
            # print(Counter(s2[left:right]))
            if Counter(s2[left:right])== s1:
                return True
            left += 1
        return False