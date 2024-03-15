# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        myList = []
        cur = list1
        cur2 = list2
        while cur:
            if cur:
                myList.append(cur.val)
                cur = cur.next
        while cur2:
            myList.append(cur2.val)
            cur2 = cur2.next
        myList.sort()
        head, tail = None, None
        for i in myList:
            item = ListNode(i)
            if head== None:
                head = item
                tail = head
            else:
                tail.next = item
                tail = tail.next
        return head
            