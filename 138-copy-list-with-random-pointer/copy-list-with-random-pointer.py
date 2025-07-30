"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr, old_new_map = head, {None:None}

        while curr:
            
            copy = Node(x=curr.val)
            old_new_map[curr] = copy

            curr = curr.next

        curr = head
        while curr:
            copy = old_new_map[curr]

            copy.next = old_new_map[curr.next]
            copy.random = old_new_map[curr.random]

            curr = curr.next

        return old_new_map[head]



