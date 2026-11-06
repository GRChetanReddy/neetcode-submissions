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
        if not head:
            return None
        d = {}
        h = head
        while h:
            d[h] = Node(h.val)
            h = h.next
        h = head
        while h:
            d[h].next = d[h.next] if h.next else None
            d[h].random = d[h.random] if h.random else None
            h = h.next
        return d[head]