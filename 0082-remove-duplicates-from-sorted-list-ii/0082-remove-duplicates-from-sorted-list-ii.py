# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        diction = {}
        myList = []
        while cur:
            if cur.val in diction:
                if cur.val in myList:
                    myList.remove(cur.val)
            else :
                diction[cur.val] = 1
                myList.append(cur.val)
            cur = cur.next
        head, tail = None, None
        for i in myList:
            item = ListNode(i)
            if not head:
                head = item
                tail = head
            else:
                tail.next = item
                tail = tail.next
        return head
       