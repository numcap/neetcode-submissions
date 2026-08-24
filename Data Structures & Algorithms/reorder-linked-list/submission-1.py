# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        - what we can do is:
            - split the linked list using fast and slow pointers
            - reverse the second linked list
            - then merge them together
        """

        # make 2 pointers that point at the start
        fast = slow = head

        # go through and iterate slow once, and fast twice 
        # to find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # take the half and create the second half
        secondHalf = slow.next
        slow.next = None

        # reverse the second half
        prev, curr = None, secondHalf

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev is now the reversed second half
        secondHalf = prev
        firstHalf = head

        # now merge them together
        while secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next

            firstHalf.next = secondHalf
            secondHalf.next = temp1

            firstHalf = temp1
            secondHalf = temp2


