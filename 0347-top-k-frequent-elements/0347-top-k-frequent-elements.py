class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        llist = []
        for num in set_nums:
            llist.append([nums.count(num), num])
        llist.sort(reverse= True)
        answer = []

        for i in range(k):
            answer.append(llist[i][1])
        return answer