# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res,n = 0,len(citations)
        low,high = 0,len(citations) - 1
        
        while low <= high:

            mid = (high + low)//2

            if citations[-mid -1] >= mid + 1:
                res= mid + 1
                low = mid + 1
            else:
                high = mid - 1

        return res