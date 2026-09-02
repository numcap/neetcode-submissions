# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        elif not q and p:
            return False

        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            # Both nodes are None -> structurally valid at this spot
            if not p_node and not q_node:
                continue
            
            # One is None or their values don't match -> trees are different
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
        
            p_queue.append(p_node.left)
            p_queue.append(p_node.right)
            q_queue.append(q_node.left)
            q_queue.append(q_node.right)

        return True