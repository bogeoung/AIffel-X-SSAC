# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            node.val , node.next.val = node.next.val, node.val
            node = node.next.next
        return head

'''
for i in range(len(head)/2):
-> object of type 'ListNode' has no len()
'''