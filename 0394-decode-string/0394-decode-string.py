class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ''
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                temp = i
                stack.append(s[i])
                i += 1
                while i < len(s) and stack:
                    if s[i] == '[':
                        stack.append(s[i])
                    elif s[i] == ']':
                        stack.pop()
                    i +=1
                i -=1 
                res.append(self.decodeString(s[temp+1:i]) * int(num))

            elif s[i].isalnum():
                res.append(s[i])
            i += 1
        return "".join(res)
