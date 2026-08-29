# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])

        m = 0

        while queue:
            node = queue.popleft()

            if node[0].left:
                queue.append((node[0].left, node[1] + 1))
            if node[0].right:
                queue.append((node[0].right, node[1] + 1))
            m = max(m, node[1] + 1)
        return m