# Definition for singly-linked list.
from typing import *
from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        deq = deque()
        while head is not None:
            deq.append(head.val)
            head = head.next

        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False

        return True
