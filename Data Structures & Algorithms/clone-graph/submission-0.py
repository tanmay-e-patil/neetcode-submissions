"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.d = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node in self.d:
            return self.d[node]
        newNode = Node(node.val)
        self.d[node] = newNode
        for n in node.neighbors:
            print(n.val)
            newNode.neighbors.append(self.cloneGraph(n))
        return newNode
        