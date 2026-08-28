# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        - we can have a 2 pointer approach where we kinda trace along the tree
        - or we can flip them from the root node, just do 
        '''
        if root is None:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp
    
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        


