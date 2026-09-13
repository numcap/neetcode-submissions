# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        q = deque([root])

        while q:
            curr_level = []
            # how to get away with mutating a list inside a for loop
            for i in range(len(q)): 
                node = q.pop()
                curr_level.append(node.val)
            
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            
            ans.append(curr_level)
            
        return ans