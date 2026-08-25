# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        string1 = ""
        string2 = ""

        while l1:
            string1 = str(l1.val) + string1
            l1 = l1.next
        while l2:
            string2 = str(l2.val) + string2
            l2 = l2.next
        
        final_num = str(int(string1) + int(string2))

        n = len(final_num) - 1

        dummy = node = ListNode()

        while n >= 0:
            node.next = ListNode(final_num[n])
            node = node.next
            n -= 1
        
        return dummy.next
