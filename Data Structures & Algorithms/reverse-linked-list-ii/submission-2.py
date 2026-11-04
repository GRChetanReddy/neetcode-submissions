# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        i = 1
        l = dummy
        while i<left:
            l = l.next
            i+=1
        i = 0
        r = dummy
        while i<right:
            r = r.next
            i+=1

        cur = l.next
        prv = r.next
        i = left
        while i<=right:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
            i+=1

        l.next = prv
        return dummy.next

            