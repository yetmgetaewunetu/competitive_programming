class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mydict = {}
        for i in range(len(s)):
            if s[i] in mydict:
                mydict[s[i]] = i
            else:
                mydict[s[i]] = i
        res = []
        left = 0
        while left < len(s):
            index = left
            right = mydict[s[left]]
            while index < right:
                if mydict[s[index]] > right:
                    right = mydict[s[index]]
                index += 1
            res.append(right - left + 1)
            left = right + 1
        return res