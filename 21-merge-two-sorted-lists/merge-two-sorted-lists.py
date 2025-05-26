# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        p1, p2, head = list1, list2, ListNode()
        prev = head

        while p1 and p2:

            if p1.val < p2.val:
                curr = ListNode(val=p1.val)
                
                p1 = p1.next
            else:
                curr = ListNode(val=p2.val)
                p2 = p2.next

            prev.next = curr
            prev = curr
        
        if p1:
            prev.next = p1
        elif p2:
            prev.next = p2
        
        return head.next


        