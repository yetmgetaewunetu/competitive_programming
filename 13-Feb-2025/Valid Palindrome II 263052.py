# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        flag = False
        l,r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                flag = True
                temp = True
                temp2 = True
                k = l +1
                j = r-1
                while k < r:
                    if s[k] != s[r]:
                        temp = False
                        break
                    k,r = k+1, r-1
                while l < j:
                    if s[l] != s[j]:
                        temp2 = False
                        break
                    l,j = l +1, j-1
                return temp or temp2
            if flag:
                break
            l,r = l+1, r-1
        return True