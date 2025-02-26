# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s  = f = cur = head
        prev = None
        res = 0
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
        prev.next = None
        prev = None
        nx = s

        if s.next:
            nx = nx.next

        while nx:
            s.next  = prev
            prev = s
            s = nx
            nx = nx.next
        s.next = prev
        h1 = head
        h2 = s
        
        while h1 and h2:
            res = max(res, h1.val+ h2.val)
            h1 = h1.next
            h2 = h2.next
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        # res = i = 0
        # mydict = {}
        # s  = f = cur = head
        # while f and f.next:
        #     s = s.next
        #     f = f.next.next
        # while cur != s:
        #     mydict[i] = cur.val
        #     cur = cur.next
        #     i += 1
        # n = i*2
        # while cur:
        #     ind = n - i -1
        #     num =  mydict[ind] + cur.val
        #     res = max(res,num)
        #     cur = cur.next
        #     i += 1
        # return res





'''
  1 2 3 4 5 6
'''