# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        r1 = head
        r2 = slow.next
        slow.next = None
        def rvrs(ll):
            if not ll or not ll.next:
                return ll
            prv = None
            cur = ll
            while cur:
                nxt = cur.next
                cur.next = prv
                prv = cur
                cur = nxt
            return prv
        r2 = rvrs(r2)
        while r2:
            temp1 = r1.next
            temp2 = r2.next
            r1.next = r2
            r2.next = temp1
            r1 = temp1
            r2 = temp2
        return