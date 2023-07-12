class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        evens = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
        llist = set(evens)
        if len(evens) == 0:
            return -1
        else:
            freq = []
            for even in llist:
                freq.append([nums.count(even), even])
            freq.sort(reverse=True)
            
            cnt =  nums.count(freq[0][1])
            answer = []
            for i in freq:
                if i[0] == cnt:
                    answer.append(i[1])
            answer.sort()
            return answer[0]