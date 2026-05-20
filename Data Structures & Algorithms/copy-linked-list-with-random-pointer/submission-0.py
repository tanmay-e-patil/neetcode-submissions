"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def printList(head):
            cur = head
            while cur:
                print("Node", cur.val, cur.next, cur.random)
                cur = cur.next
            return
        cur = head
        while cur:
            new = Node(cur.val, cur.next)
            cur.next = new
            cur = cur.next.next
        
        # cur = head.next
        # while cur:
            
        #     cur.next = cur.
        #     cur = cur.next.next
        
        cur = head
        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next
                
            cur = cur.next.next
        
        printList(head)
        
        
        new_head = Node(0)
        new_cur = new_head
        cur = head
        while cur:
            new_cur.next = cur.next
            cur.next = cur.next.next
            
            cur = cur.next
            new_cur = new_cur.next
        
        return new_head.next
    
        



        