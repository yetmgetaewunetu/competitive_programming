# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        x = []
        while cur:
            if cur.val not in x:
                x.append(cur.val)
            cur = cur.next
        head = None
        tail = head
        for i in x:
            item = ListNode(i)
            if head is None:
                head = item
                tail = item
            else:
                tail.next = item
                tail = tail.next

        return head
                