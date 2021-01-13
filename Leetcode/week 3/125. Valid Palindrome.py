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
        # 덱의 제일 앞과 뒤가 같은지 비교
        while len(strings) > 1: # 제일 앞과 뒤를 비교할 것이기 때문에 한개가 남으면 빠져나감
            if strings.popleft() != strings.pop():
                return False
        return True

test = Solution()
print(test.isPalindrome("race is a car"))