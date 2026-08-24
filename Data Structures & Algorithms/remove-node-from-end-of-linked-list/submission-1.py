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

        if head.next is None and n == 1:
            return 
        
        dummy = first = second = prev = head

        for i in range(n):
            second = second.next
        
        if second is None:
            return head.next

        while second:
            prev = first
            second = second.next
            first = first.next

        prev.next = first.next

        return dummy

