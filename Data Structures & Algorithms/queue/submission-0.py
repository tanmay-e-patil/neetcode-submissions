class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
            
        

    def append(self, value: int) -> None:
        node = Node(value)
        prev, nxt = self.tail.prev, self.tail
        node.next, node.prev = nxt, prev
        prev.next, nxt.prev = node, node
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        prev, nxt = self.head, self.head.next
        node.next, node.prev = nxt, prev
        prev.next, nxt.prev = node, node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.tail.prev
        val = node.val

        prev = node.prev
        prev.next = self.tail
        self.tail.prev = prev
        return node.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.head.next
        val = node.val
        nxt = node.next
        
        self.head.next = nxt
        nxt.prev = self.head
        return val
        
