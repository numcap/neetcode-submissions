# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], r: List[int]) -> Optional[TreeNode]:

        indicies = {val: idx for idx, val in enumerate(inorder)}

        pre_idx = 0

        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None

            root = TreeNode(preorder[pre_idx])
            mid = indicies[preorder[pre_idx]]
            pre_idx += 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
