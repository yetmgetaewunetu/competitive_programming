# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val 
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy_head, self.dummy_tail = Node("dummy","none"),Node("dummy","none")
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.lru_dic = {}

    def insert_at_the_end(self,node):
        old_node = self.dummy_tail.prev
        old_node.next = node
        node.prev = old_node
        node.next = self.dummy_tail
        self.dummy_tail.prev = node

    def delete_node(self,node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def get(self, key: int) -> int:
        if key not in self.lru_dic:
            return -1
        node = self.lru_dic[key]
        self.delete_node(node)
        self.insert_at_the_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lru_dic:
            node = self.lru_dic[key]
            node.val = value
            self.delete_node(node)
            self.insert_at_the_end(node)
            self.lru_dic[key] = node
            return

        if self.capacity == len(self.lru_dic):
            old_node = self.dummy_head.next
            self.delete_node(old_node)
            del self.lru_dic[old_node.key]
        node = Node(key,value)
        self.lru_dic[key] = node
        self.insert_at_the_end(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)