from typing import List

class Node:
    def __init__(self, val: int, next_node: 'Node' = None): # Renamed 'next' to 'next_node' to avoid conflict with Python's 'next()' built-in function
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Initialize with a dummy head node. This simplifies operations, especially insertions and deletions at the beginning.
        self.head = Node(0) 
        self.size = 0

    def get(self, index: int) -> int:
        # Check for out-of-bounds index
        if index < 0 or index >= self.size:
            return -1
        
        # Start traversal from the node AFTER the dummy head
        cur = self.head.next
        for _ in range(index): # Traverse 'index' times to reach the desired node
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        # Insert new node right after the dummy head
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        self.size += 1
        
    def insertTail(self, val: int) -> None:
        cur = self.head
        # Traverse to the last node (the one whose 'next' is None)
        while cur.next:
            cur = cur.next
        
        # Append the new node
        cur.next = Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        # Check for out-of-bounds index
        if index < 0 or index >= self.size:
            return False
        
        # Start traversal from the dummy head to find the node BEFORE the one to be removed
        cur = self.head
        for _ in range(index): # Traverse 'index' times to reach the node before the target
            cur = cur.next
        
        # Node to be removed is cur.next
        node_to_remove = cur.next
        cur.next = node_to_remove.next # Link current node to the node after the one being removed
        node_to_remove.next = None # Detach the removed node
        del node_to_remove # Explicitly delete (optional in Python due to garbage collection)
        self.size -= 1
        return True
        
    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next # Start from the actual first node
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res