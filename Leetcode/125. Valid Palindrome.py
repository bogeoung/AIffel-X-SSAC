from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        # 소문자로 만들기
        s = s.lower()
        # 문자를 넣을 deque 선언
        strings = deque()

        # 소문자로 통일한 문장에서 영어, 한글만 strings 덱에 추가
        for i in s:
            if i.isalnum():
                strings.append(i)

        print(strings)
       # 덱의 제일 앞과 뒤가 같은지 비교
        while len(strings) > 1:      # 제일 앞과 뒤를 비교할 것이기 때문에 한개가 남으면 빠져나감
            if strings.popleft() != strings.pop():
                return False
        return True
