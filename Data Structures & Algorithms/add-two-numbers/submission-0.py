# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        while l1:
            n1 = str(l1.val)+n1
            l1 = l1.next
        n2 = ''
        while l2:
            n2 = str(l2.val)+n2
            l2 = l2.next
        n3 = str(int(n1)+int(n2))
        l3 = ListNode()
        l = l3
        for i in range(len(n3)-1, 0, -1):
            l.val = int(n3[i])
            l.next = ListNode()
            l = l.next
        l.val = int(n3[0])
        return l3

        