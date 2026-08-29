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

        m = 0 # max level count

        while queue:
             # get node ande depth from tuple
            node, depth = queue.popleft()

            # append the children and the depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
            m = max(m, depth + 1) # keep track of the max depth
        return m