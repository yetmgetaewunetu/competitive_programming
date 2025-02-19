# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        temp = cur
        while temp:
            if temp.val != cur.val:
                cur.next = temp
                cur = cur.next
            temp = temp.next
        else:
            if cur:
                cur.next = None
        return head