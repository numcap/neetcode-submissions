# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        same = False

        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            if t1 and t2 and t1.val == t2.val:
                return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)
            else:
                return False

        
        def dfs(node): 
            nonlocal subRoot
            nonlocal same
            if not node or same:
                return 

            same = sameTree(node, subRoot)
            dfs(node.left)
            dfs(node.right)
            return node

        dfs(root)
        return same