# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # q = deque()
        # q.append([root, 0])

        # while q:
        #     node, level = q.popleft()
            
        def dfs(node):
            if not node:
                return [True, 0]
            l,left_level = dfs(node.left)
            r, right_level = dfs(node.right)

            return [l and r and abs(left_level - right_level) <= 1, 1+ max(left_level, right_level)]
        
        return dfs(root)[0]
        