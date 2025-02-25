# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/


class BrowserHistory:
    class Node:
        def __init__(self, val):
            self.val= val
            self.prev = None
            self.next = None
            
    def __init__(self, homepage: str):
        home = self.Node(homepage)
        self.dummy_head = self.Node(None)
        self.dummy_tail = self.Node(None)
        self.dummy_head.next = home
        self.dummy_tail.prev = home
        home.next = self.dummy_tail
        home.prev = self.dummy_head
        self.cur = home


    def visit(self, url: str) -> None:
        node = self.Node(url)
        self.cur.next = node
        node.prev = self.cur
        node.next = self.dummy_tail
        self.dummy_tail.prev = node
        self.cur = self.cur.next


    def back(self, steps: int) -> str:
        for i in range(steps):
            self.cur = self.cur.prev
            if self.cur==self.dummy_head:
                self.cur = self.dummy_head.next
                return self.cur.val
        return self.cur.val


    def forward(self, steps: int) -> str:
        for i in range(steps):
            self.cur = self.cur.next
            if self.cur == self.dummy_tail:
                self.cur = self.dummy_tail.prev
                return self.cur.val
        return self.cur.val

 

    




# class BrowserHistory:

#     def __init__(self, homepage: str):
#         # self.dummy_head = Node(None)
#         # self.dummy_tail = Node(None)
#         # self.dummy_head.next = self.dummy_tail
#         # self.dummy_tail.prev = self.dummy_head
#         # self.cur = self.dummy_head
#         self.arr = [homepage]
#         self.cur = 0
#     def visit(self, url: str) -> None:
#         # prev = self.dummy_tail.prev
#         self.cur += 1
#         self.arr.insert(self.cur,url)
#         self.arr = self.arr[:self.cur+1]
#         # print(self.arr,self.cur)
#     def back(self, steps: int) -> str:
#         if self.cur - steps <0:
#             self.cur = 0
#             return self.arr[self.cur]
#         self.cur = self.cur -steps
#         return self.arr[self.cur]

#     def forward(self, steps: int) -> str:
#         if self.cur + steps < len(self.arr):
#             self.cur += steps
#             return self.arr[self.cur]
#         self.cur = len(self.arr) -1
#         return self.arr[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)