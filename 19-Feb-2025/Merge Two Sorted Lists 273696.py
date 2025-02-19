# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        head =  cur =None
        while left != None and right != None:
            if left.val <= right.val:
                if not cur:
                    head = cur = left
                else:
                    cur.next = left
                    cur = cur.next
                left = left.next
            else:
                if not cur:
                    head = cur = right
                else:
                    cur.next = right
                    cur = cur.next
                right = right.next
        while left:
            if not cur:
                    head = cur = left
            else:
                cur.next = left
                cur = cur.next
            left = left.next
        while right is not None:
            if not cur:
                    head = cur = right
            else:
                cur.next= right
                cur = cur.next
            right = right.next
        return head