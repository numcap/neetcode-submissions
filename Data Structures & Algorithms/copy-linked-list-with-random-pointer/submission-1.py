"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = random_dummy = new_list = Node(0)

        head_dummy = head

        nodes = {} # old random nodes: new random nodes

        while head:
            new_list.next = Node(head.val)
            new_list = new_list.next
            nodes[head] = new_list
            # print(head.val)
            # print(head.random)
            head = head.next
        # return dummy.next

        while head_dummy:
            random_dummy.next.random = nodes.get(head_dummy.random)
            random_dummy = random_dummy.next
            head_dummy = head_dummy.next

        return dummy.next

            

