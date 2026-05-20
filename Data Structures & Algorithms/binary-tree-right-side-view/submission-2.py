# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        level = 0
        stack.append(tuple((level, root)))
        res = []
        while stack:
            elem = stack.pop()
            l, node = elem
            
            if l == level:
                res.append(node.val)
                level += 1
            if node.left:
                stack.append((l + 1, node.left))
            if node.right:
                stack.append((l + 1,node.right))
        return res
                
        
        