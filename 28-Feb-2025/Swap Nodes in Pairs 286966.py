# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        first = head
        second = head.next
        third  = second.next
        while second:
            second.next = first
            first.next = None
            cur.next = second
            cur = first
            if third and third.next:
                first = third
                second = third.next
                third = second.next
            else:
                cur.next = third
                return dummy.next
        return dummy.next