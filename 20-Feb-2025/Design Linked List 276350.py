# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        #[1,2,3,4,5]
        self.head = None
        self.tail = None
        self.len = 0
    def get(self, index: int) -> int:
        cur = self.head
        if index >= self.len:
            return -1
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head  = newNode
        self.len += 1
        if not self.tail:
            self.tail = self.head
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head= newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.len += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index >= self.len:
            return -1
        cur = self.head
        newNode = Node(val)
        for i in range(index-1):
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode
        self.len += 1
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return -1
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        if self.len == 1:
            cur = cur.next
        else:
            cur.next = cur.next.next
        self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)