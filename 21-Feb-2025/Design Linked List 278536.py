# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class MyLinkedList:
    class Node:
        def __init__(self,val):
            self.val  = val
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index):
            cur = cur.next
            # print(cur.val,index)
            if not cur:
                break
        else:
            if cur:
                return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val)
        if not self.head:
            self.head= newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = self.Node(val)
        cur = self.head
        if not self.head:
            self.head = newNode
        else:
            while cur.next:
                cur = cur.next
            cur.next = newNode


    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head and index>0:
            return
        dummy = self.Node(None)
        newNode = self.Node(val)
        dummy.next = self.head
        cur = dummy
        for _ in range(index):
            cur = cur.next
            if not cur:
                break
        else:
            newNode.next = cur.next
            cur.next = newNode
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return 
        dummy  = self.Node(None)
        dummy.next = self.head
        cur = dummy
        for _ in range(index):
            cur = cur.next
            if not cur:
                break
        else:
            if cur.next:
                # print(cur.next.next)
                cur.next = cur.next.next

            elif cur:
                cur.next = None
             
        self.head = dummy.next
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)