# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry, digit, dummy_head = 0, 0, ListNode()

        curr = dummy_head

        while l1 or l2:

           tot = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

           digit = tot % 10
           carry = tot //10

           curr.next = ListNode(val=digit)

           l1 = l1.next if l1 else None
           l2 = l2.next if l2 else None
           curr = curr.next

        if carry !=0:
            curr.next = ListNode(val=carry)
        
        return dummy_head.next
