# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        def permute(num,cur):
            # print(num,cur,temp)
            if cur == k:
                ans.append(temp.copy())
                return

            for j in range(num,n+1):
                temp.append(j)
                permute(j+1,cur + 1)
                temp.pop()

        permute(1,0)
        return ans
