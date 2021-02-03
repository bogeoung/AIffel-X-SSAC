from typing import *
class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None
    def push(self,item):
        self.last = Node(item,self.last)
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

# 못풀음
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
            stack = Stack()
            stack.push(T[0])
            result = []

            for num in T:
                count = 0
                while stack.pop() < num:
                    count +=1
                stack.push(nu)
                result.append(count)
