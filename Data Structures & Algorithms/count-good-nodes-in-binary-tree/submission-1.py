# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        greatest = -float("inf") # or -101
        num = 0

        def dfs(node, greatest):
            if not node:
                return

            nonlocal num
            # print("node", node.val)
            # print("greatest before", greatest)

            if node.val >= greatest:
                greatest = node.val
                num += 1

            # print("greatest after", greatest)
            # print("\n\n")


            dfs(node.left, greatest)
            dfs(node.right, greatest)
            return
        
        dfs(root, greatest)
        return num