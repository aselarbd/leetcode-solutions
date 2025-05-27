# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find mid point
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # in place alter linklists
        second = slow.next
        slow.next = prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # combine link lists front and back
        front, back = head, prev

        while back:
            front_tmp, back_tmp = front.next, back.next

            front.next = back
            back.next = front_tmp

            front, back = front_tmp, back_tmp
        