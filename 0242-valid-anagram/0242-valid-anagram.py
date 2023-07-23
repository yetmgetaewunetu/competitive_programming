class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        List = []
        Listt = []
        booli = False
        if len(s) == len(t):
            for i in set(t):
                List.append(s.count(i))
                Listt.append(t.count(i))
            print(List, Listt)
     
            for i in range(len(List)):
                if List[i] == Listt[i]:
                    booli = True
                else:
                    booli = False
                    break
        return booli