# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()

        res = 0
        l = 0
        for r in range(len(nums)):
            while min_q and nums[r]< min_q[-1]:
                min_q.pop()

            while max_q and nums[r] > max_q[-1]:
                max_q.pop()

            min_q.append(nums[r])
            max_q.append(nums[r])
            while max_q[0]- min_q[0] > limit:
                if nums[l] == min_q[0]:
                    min_q.popleft()
                if nums[l] == max_q[0]:
                    max_q.popleft()
                l += 1
            res = max(res,r-l+1)
            # print(min_q,max_q,res,l,r)
        return res
