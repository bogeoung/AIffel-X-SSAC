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

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # 딕셔너리를 이용해 매핑테이블 형성
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        print(table)
        for char in s:
            # table에 있는 경우 -> ), }, ]만 해당
            if char not in table:
                stack.append(char)

            # table에 존재하지 않거나, table의 value값이 stack에 최상단과 짝이 안맞을 경우
            elif not stack or table [char] != stack.pop():
                return False

        # 예외처리
        return len(stack) == 0

'''
class Solution:
    def isValid(self, s: str) -> bool:
        #string의 개수가 홀수개면 False 리턴
        if len(s)%2 != 0 :
            return False
        count = 0
        my_stack = Stack()
        for char in s:
            print(char)
            if char == "[" or "(" or "{":
                my_stack.push(char)
                count = count+1
            elif char == "]" or ")" or "}":
                temp = stack.pop()
                if char == "]" and temp != "[":
                    return False
                elif char == ")" and temp != "(":
                    return False
                elif char == "}" and temp != "{":
                    return False

        return True
'''
test = Solution()
s = "]"
print(test.isValid(s))

