# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0]*k
        self.front = self.last = -1
        self.capacity = k
        self.length = 0
    def insertFront(self, value: int) -> bool:
        if self.length == self.capacity:
            return False

        self.front -= 1
        if self.front == -1:
            self.front = self.capacity -1

        if self.length == 0:
            self.last = self.front = 0

        self.length +=1
        self.deque[self.front] = value
        return True


    def insertLast(self, value: int) -> bool:
        if self.length == self.capacity:
            return False

        self.last = (self.last + 1) % self.capacity

        if self.length == 0:
            self.front = self.last = 0
            
        self.length +=1
        self.deque[self.last] = value
        return True

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False

        temp = self.deque[self.front]
        self.front = (self.front + 1) % self.capacity
        self.length -=1
        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        temp = self.deque[self.last]
        self.last -=1
        if self.last == -1:
            self.last = self.capacity -1
        self.length -=1
        return True

    def getFront(self) -> int:
        if not self.length:
            return -1 
        return self.deque[self.front]

    def getRear(self) -> int:
        if not self.length:
            return -1 
        return self.deque[self.last]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()