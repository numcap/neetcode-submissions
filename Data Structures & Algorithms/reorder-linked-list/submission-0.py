# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        problem: we want to reorder by [0, n-1, 1, n-2, 2]

        potential solution: 2 pointer solution
        """

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev
        while second:
            temp1, temp2 = head.next, second.next
            head.next = second
            second.next = temp1
            head, second = temp1, temp2




