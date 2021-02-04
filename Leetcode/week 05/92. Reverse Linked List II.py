# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head
        num = m - n + 1
        #m 번째까지 이동
        for i in range(m):
            node = node.next

        end = node.next
        for i in range(num):
            tmp, node.next, end.next = node.next, end.next, end.next.next
            node.next.next = tmp
        return node.next

# 푸는데 실패함