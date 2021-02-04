# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev : 뒤집힌 연결리스트의 처음을 가리킴
        # node : 입력된 ListNode의 head로 초기화
        node, prev = head, None
        while node:
            # next 변수에 node.next를 이용하여 다음 노드를 저장
            # node.next = prev는 백트래킹을 위해서 존재
            next, node.next = node.next, prev
            # prev에 현재 노드를 저장, node에 다음 node를 저장
            prev, node = node, next

        return prev