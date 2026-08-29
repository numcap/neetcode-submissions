# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check root = Nonde edge case 
        if not root:
            return
        
        # intialize the doubled ended queue with the root as the first element
        queue = deque([root])

        while queue:
            # pop the left side of the queue, so the its in order going
            # level by level down the tree
            node = queue.popleft()

            # swap sides
            node.left, node.right = node.right, node.left

            # check if there is a left and right node, if there is append
            # them to the right side of the queue, so that they will be checked 
            # when going to the next level
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return root
