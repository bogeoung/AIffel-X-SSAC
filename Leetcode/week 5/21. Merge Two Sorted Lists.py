# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = l1.val
        else:
            head = l2.val

        templist = ListNode(head)

        while True:
            print("l1.val", l1.val, "l2.val", l2.val)

            if l1.val < l2.val:
                templist.next = ListNode(l1.val)
                if l1.next is not None:
                    l1 = l1.next
                    templist = templist.next
                else:
                    break

            else:
                templist.next = ListNode(l2.val)
                if l2.next is not None:
                    l2 = l2.next
                    templist = templist.next
                else:
                    break

            print("templist", templist)

        return templist
