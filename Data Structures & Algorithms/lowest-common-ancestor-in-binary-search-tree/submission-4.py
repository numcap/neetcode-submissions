# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        lca = TreeNode()

        def check(node):
            if not node:
                return False

            if q == node or p == node:
                return True
            else:
                return check(node.left) or check(node.right)

        def dfs(node):
            nonlocal lca
            if not node:
                return
            
            left_check = check(node.left)
            right_check = check(node.right)
            curr_node = q == node or p == node

            if (left_check and right_check) or (left_check and curr_node) or (right_check and curr_node):
                lca = node
            
            if left_check and not right_check:
                dfs(node.left)
            elif not left_check and right_check:
                dfs(node.right)
            return

        dfs(root)
        return lca
        
