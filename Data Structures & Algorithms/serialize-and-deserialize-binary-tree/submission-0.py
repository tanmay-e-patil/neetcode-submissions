# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def helper(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)
        return ','.join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        idx = 0

        def helper():
            nonlocal idx
            if vals[idx] == "N":
                idx += 1
                return None
            node = TreeNode(int (vals[idx]))
            idx += 1
            node.left = helper()
            node.right = helper()
            return node
        return helper()

        return None
