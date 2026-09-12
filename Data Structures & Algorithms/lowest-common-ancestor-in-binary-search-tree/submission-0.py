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
            print("node", node.val)
            left_check = check(node.left)
            print("left_check", left_check)
            right_check = check(node.right)
            print("right_check", right_check)
            curr_node = q == node or p == node
            print("curr_node", curr_node)
            print("\n\n")

            if (left_check and right_check) or (left_check and curr_node) or (right_check and curr_node):
                lca = node
            
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return lca
        
