# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None

        front = back = prev = head 

        for _ in range(n):
            front = front.next
        
        if front is None:
            return head.next
        
        while front:
            prev = back
            back = back.next
            front = front.next

        prev.next = back.next

        return head
