# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - here we can use 2 pointers to find the nth last node by:
            - keeping the first pointer on the head then taking the second pointer and separating it from the head by n
            - now we continue until the second pointer hits null and the first pointer would be the nth node from the end
        """

        # edge case where there is only 1 node
        if head.next is None and n == 1:
            return
        
        prev = first = second = head

        # moving second pointer n away from start
        for i in range(n):
            second = second.next
        
        # if second pointer is out of bounds it means that the first 
        # node is being removed
        if second is None:
            return head.next

        # move pointers until second is null
        while second:
            prev = first
            first = first.next
            second = second.next

        prev.next = first.next

        return head





