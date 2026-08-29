# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS recursive approach
        if root is None:
            return
        
        # invert here
        root.left, root.right = root.right, root.left
    
        # recursively go to the very left node
        self.invertTree(root.left)
        # recursively go to the very right node
        self.invertTree(root.right)
        return root
        


