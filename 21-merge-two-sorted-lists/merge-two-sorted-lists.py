# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            list1
        
        head, a, b = ListNode(), list1, list2
        curr = head

        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
                curr = curr.next
            elif a.val > b.val:
                curr.next = b
                b = b.next
                curr = curr.next
            else:
                curr.next = a
                a = a.next
                curr = curr.next
                curr.next = b
                b = b.next
                curr = curr.next
        if a:
            curr.next = a
        if b:
            curr.next = b
        
        return head.next




