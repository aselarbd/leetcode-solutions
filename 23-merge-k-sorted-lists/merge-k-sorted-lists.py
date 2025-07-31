# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        dummy_head = ListNode()
        curr = dummy_head

        state = [l.val if l else None for l in lists]

        while not all(s is None for s in state):

            min_value = min(x for x in state if x is not None )  
            min_index = state.index(min_value)

            curr.next = ListNode(val=min_value)

            next_list_node = lists[min_index].next if lists[min_index] else None
            state[min_index] = next_list_node.val if next_list_node else None

            lists[min_index] = next_list_node if next_list_node else None
            curr = curr.next

        return dummy_head.next
