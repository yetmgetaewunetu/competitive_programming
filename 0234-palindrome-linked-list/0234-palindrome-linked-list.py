# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        stack1 = []
        while cur:
            stack1.append(cur.val)
            cur = cur.next
        stack2 = []
        for i in stack1:
            stack2.insert(0, i)
            
        return stack1 == stack2