# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        myList = []
        for i in range (right):
            if i >= left-1:
                myList.append(cur.val)
            cur = cur.next
        myList.reverse()
        cur = head
        for i in range(right):
            if i>= left-1:
                cur.val = myList[i - left + 1]
            cur = cur.next
        return head