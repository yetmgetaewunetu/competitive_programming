# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i =="*":
                stack.pop()
            elif i != "*":
                stack.append(i)
        return "".join(stack)