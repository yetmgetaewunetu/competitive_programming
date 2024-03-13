class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        keysli = list(count.keys())
        ans = []
        n = len(nums)//3
        for k in keysli:
            if count[k] > n:
                ans.append(k)
        return ans