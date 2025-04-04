# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # offset = min(nums)
        # buckets = [[i,0] for i in range(offset,max(nums) - offset + 2)]

        # for num in nums:
        #     buckets[num - offset][1] += 1
        
        # for i in range(k):
            
        #     for j in range(len(buckets)-1):

        #         if buckets[j][1] > buckets[j+1][1]:
        #             buckets[j],buckets[j+1] = buckets[j+1],buckets[j]

        # res = [buckets[i][0] for i in range(-1,-k-1,-1)]

        # return res




        cnt = Counter(nums)
        sor = [[v,k] for k,v in cnt.items()]
        sor.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(sor[i][1])
        return res