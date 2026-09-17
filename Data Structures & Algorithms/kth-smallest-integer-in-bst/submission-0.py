# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            nonlocal count, ans
            if not node:
                return

            dfs(node.left)  # takes you to the most left branch
            if count == 0:
                return
            count -= 1
            if count == 0:
                ans = node.val
            dfs(node.right)
            return

        count = k
        ans = 0
        dfs(root)
        return ans
