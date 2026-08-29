# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recursive function
        def checkDepth(node):
            # base case, in this case, is a number that 
            # is because there are no children nodes
            if not node:
                return 0

            # we want to return the current node we are at, 
            # along with the next 2 child nodes' height
            # which would just be 1 + their childrens nodes
            return 1 + max(checkDepth(node.left), checkDepth(node.right))

        return checkDepth(root)