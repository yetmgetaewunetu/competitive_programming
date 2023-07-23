class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for i in s:
            if i.isalnum():
                string += i
        rever = []
        for i in string:
            rever.insert(0, i)
        ans = ''
        for i in rever:
            ans += i


        return True if ans.lower() == string.lower() else False