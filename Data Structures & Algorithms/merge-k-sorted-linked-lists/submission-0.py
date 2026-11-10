# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists)>1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            dummy = ListNode()
            l3 = dummy
            while l1 and l2:
                l3.next = ListNode()
                l3 = l3.next
                if l1.val>=l2.val:
                    l3.val = l2.val
                    l2 = l2.next
                else:
                    l3.val = l1.val
                    l1 = l1.next
            if l1:
                l3.next = l1
            elif l2:
                l3.next = l2 
            lists.append(dummy.next)

        return lists[0]
