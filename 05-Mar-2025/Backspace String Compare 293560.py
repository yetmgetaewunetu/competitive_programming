# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1,stack2 = [],[]
        for i in s:
            if i =="#" and stack1:
                stack1.pop()
            elif i != "#":
                stack1.append(i)

        for i in t:
            if i =="#" and stack2:
                stack2.pop()
            elif i != "#":
                stack2.append(i)
        return True if stack1 == stack2 else False