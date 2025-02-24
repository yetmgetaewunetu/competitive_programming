# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_part(self, cur,last):
        init = cur
        prev = None
        nx = cur
        if cur:
            nx = cur.next
        while cur != last:
            cur.next = prev
            prev = cur
            cur = nx
            nx = nx.next
        cur.next = prev
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        first = head
        cur = head
        temp = None
        dummy = ListNode(None)
        h = dummy
        while cur:
            for i in range(k):
                if not cur:
                    break
                temp = cur
                cur = cur.next
            else:
                if temp:
                    f = self.reverse_part(first,temp)
                    # print(f.val,f.next.val,first.val)
                    h.next = f
                    h = first
                    # nodes.append(f)
                    first = cur
                    continue
            # nodes.append(first)
            h.next = first
        return dummy.next



        # cur = dummy
        # for node in nodes:
        #     item = node
        #     while item:
        #         cur.next = item
        #         cur = cur.next
        #         item = item.next
        # return dummy.next
            