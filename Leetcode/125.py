from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 소문자로 만들기
        s = s.lower()
        # 문자를 넣을 deque
        strings = deque()

        for i in s:
            if s.isalnum() is True:
                strings.append(i)

        while len(strings) >= 2:
            if strings.popleft() != strings.pop():
                return False
        return True