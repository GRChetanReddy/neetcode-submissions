# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        h = dummy
        for _ in range(left-1):
            h = h.next

        prev = h
        cur = h.next
        i = 0
        while right-left+1>i:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            i+=1

        x = h.next
        h.next = prev
        x.next = cur
        
        return dummy.next
            