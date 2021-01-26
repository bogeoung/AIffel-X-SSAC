# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        HOL = head
        JJAK = head.next
        JJAK_head = head.next

        # 반목문의 조건절이 왜 JJAK 기준일까?
        while JJAK and JJAK.next:
            HOL.next = HOL.next.next
            JJAK.next = JJAK.next.next
            HOL = HOL.next
            JJAK = JJAK.next

        HOL.next = JJAK_head
        return head
        # 왜 HOL을 return 하는게 아니라 head를 리턴하는지 잘 모르겠음.