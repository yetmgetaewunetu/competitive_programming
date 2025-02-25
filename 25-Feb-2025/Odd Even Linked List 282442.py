# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = True
        odd = ListNode(None)
        odd_tail = odd
        even = ListNode(None)
        even_tail = even

        cur = head
        while cur:
            if flag:
                odd_tail.next = cur
                odd_tail = odd_tail.next
            else:
                even_tail.next = cur
                even_tail = even_tail.next
            flag = not flag
            prev = cur
            cur = cur.next
            prev.next = None

        odd_tail.next = even.next
        # even.next = None
        return odd.next