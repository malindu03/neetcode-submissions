# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = res_tail = ListNode(0)
        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val < current2.val:
                res_tail.next = current1
                res_tail = current1
                current1 = current1.next
            else:
                res_tail.next = current2
                res_tail = current2
                current2 = current2.next

        if current1 is None:
            while current2 is not None:
                res_tail.next = current2
                res_tail = current2
                current2 = current2.next
        elif current2 is None:
            while current1 is not None:
                res_tail.next = current1
                res_tail = current1
                current1 = current1.next
            

        return dummy_head.next

