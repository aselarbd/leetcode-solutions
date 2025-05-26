# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        
        if head.next is None:
            return False

        slow, fast = head, head.next.next

        while fast:
            if fast == slow:
                return True
            
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next

        return False



        