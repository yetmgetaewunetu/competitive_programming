class Solution:
    def similarPairs(self, words: List[str]) -> int:
        List = []
        for i in range(len(words)):
            k = []
            for j in words[i]:
                if j not in k:
                    k.append(j)
            k.sort()
            List.append(k)
        List.sort()
        
        optional = []
        count = []
        for i in range(len(List)):
            cnt = 1
            for j in range(i + 1, len(List)):
                if  List[i] == List[j]:
                    optional.append(List[i])
                    cnt += 1
            count.append(cnt) if cnt > 1 else count.append(0)

        return len(optional)