# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        for i in range(n-1):
            right = right.next
        # print(right.val,cur.val)
        while right.next:
            right = right.next
            cur= cur.next
        cur.next = cur.next.next
        return dummy.next