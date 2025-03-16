# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        cur_min = 0
        for i,num in enumerate(nums):
            
            while stack and stack[-1][1] <= num:
               
                if len(stack) >=2 and stack[-1][1] > stack[-2][2]:
                    return True
                stack.pop()
            cur_min = cur_min if num > nums[cur_min] else i
            stack.append([i,num,nums[cur_min]])
        
        while len(stack) >=2:
            if stack[-1][1] > stack[-2][2]:
                return True
            stack.pop()
        return False

