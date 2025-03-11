# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+*-/':
                stack.append(int(i))
            elif i in '+-*':
                value = eval(str(stack[-2]) + i + str(stack[-1]))
                stack.pop()
                stack[-1] = value
            else:
                value = abs(stack[-2])// abs(stack[-1])
                if stack[-1] < 0 < stack[-2] or stack[-2] < 0 < stack[-1]:
                    value = -1 * value
                stack.pop()
                stack[-1] = value
                
                    
        return int(stack[0])