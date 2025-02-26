# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        rem = 0
        prev = None
        while h1 and h2:
            num = h1.val + h2.val + rem
            if num  >= 10:
                rem= 1
                num = num -10
            else:
                rem = 0
            h1.val = num
            prev = h1
            h1 = h1.next
            h2 = h2.next
        while h2:
            num = h2.val + rem
            if num >= 10:
                rem = 1
                num = num-10
            else:
                rem = 0
            prev.next = ListNode(num)
            prev = prev.next
            h2 = h2.next
        while h1:
            num = h1.val + rem
            if num >= 10:
                rem = 1
                num = num-10
            else:
                rem = 0
            prev = h1
            h1.val = num 
            h1 = h1.next
        if rem:
            prev.next = ListNode(rem)
        return l1           
