class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = ''
        idx = 0
    
        for i in range(len(spaces)):
            
                
            l+= s[idx:spaces[i]] + ' '
            idx = spaces[i]
        return l + s[spaces[-1]:]
        