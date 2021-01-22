# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        templist = ListNode()

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while True:
            if l1.val < l2.val:
                templist.next = ListNode(l1.val)
                l1 = l1.next

            else:
                templist.next = ListNode(l2.val)
                l2 = l2.next
