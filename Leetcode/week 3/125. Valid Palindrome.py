from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 소문자로 만들기
        s = s.lower()
        # 문자를 넣을 deque
        strings = deque()

        # 소문자로 통일한 문장에서 영어, 한글만 strings 덱에 추가
        for i in s:
            if i.isalnum(): # if i.isalnum() is True은 속도가 더 느림
                strings.append(i)
        # 덱의 제일 앞과 뒤가 같은지 비교
        while len(strings) > 1: # 제일 앞과 뒤를 비교할 것이기 때문에 한개가 남으면 빠져나감
            if strings.popleft() != strings.pop():
                return False
        return True

        ''' Another Answer
        s = s.lower() 
        s = re.sub('^a-z0-9]','',s) 
        return s = s[::-1]
        
        1. 소문자로 바꿈
        2. 정규표현식을 통해 불필요한 문자를 제거. 
           ^은 not을 의미 -> a-z 혹은 0-9가 아니면 공백으로 치환한다는 의미
        3. s와 s[::-1]가 같은지를 비교하여 Ture 혹은 False리턴
           이때 s[::-1]은 문자열 슬라이스의 한 기능으로 문자열을 뒤집는다.
        '''