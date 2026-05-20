# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(node, mx_value = -float('inf')):
            nonlocal count
            if not node:
                return
            # print(node.val, mx_value)
            if node.val >= mx_value:
                mx_value = max(mx_value, node.val)
                count += 1
                # print(count)
            helper(node.left, mx_value)
            helper(node.right, mx_value)
        helper(root)
        return count


        