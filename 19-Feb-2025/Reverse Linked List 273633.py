# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head.next
        prev = head
        nx = None
        if cur.next:
            nx = cur.next
        while nx and nx.next is not None:
            cur.next = prev
            prev = cur
            cur = nx
            nx = nx.next
        if nx:
            nx.next = cur
        cur.next = prev
        head.next = None
        if nx:
            return nx 
        else:
            return cur
