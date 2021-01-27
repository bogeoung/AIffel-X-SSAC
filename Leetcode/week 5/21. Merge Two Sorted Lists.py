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
                templist.next = l1
                # next는 다음 연결리스트의 주소를 가리키는 것임.
                # templist.next = ListNode(l1.val)
                # 따라서 ListNode(l1.val)이 아닌 l1을 넣어야 함.
                if l1.next is not None:
                    l1 = l1.next
                else:
                    break

            else:
                templist.next = l2
                if l2.next is not None:
                    l2 = l2.next
                else:
                    break
            templist = templist.next
            print("templist", templist)

        return templist

# 못풀음