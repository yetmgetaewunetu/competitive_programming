# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checkValid(limit):
            cur = 0
            ks = 1
            for num in nums:
                cur += num

                if num > limit:
                    return False

                if cur > limit:
                    ks += 1
                    cur = num

            return ks <= k

        low,high = min(nums),sum(nums)
        res = high

        while low <= high:

            mid = (low + high) //2

            if checkValid(mid):
                res = mid
                high = mid -1
            else:
                low = mid + 1

        return res