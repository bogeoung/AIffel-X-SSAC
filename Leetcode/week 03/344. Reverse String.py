class Solution:
    def reverseString(self, s) -> None:
        # 반복할 횟수를 정하기 위해 전체길이의 2를 나눈 몫을 구함
        time = len(s)/2
        # 바꿀 문자열의 위치를 지정할 변수 count 선언
        count = 0
        while time >= 1 :
            time -= 1 # 무한루프를 막기 위해 time 감소
            temp = s[count] # temp라는 임시 변수에 s[count]값을 저장 후, 값을 교환함
            s[count] = s[-(count+1)] # 파이썬에서는 s[count], s[-(count+1)] = s[-(count+1), s[count]로 사용 가능하다고 함.]
            s[-(count+1)] = temp
            count += 1

        ''' Another Answer 1
        def reverseString(self, s:List[str]) -> None:
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        '''
        ''' Another Answer 2
        def reverseString(self, s:List[str]) -> None:
            s.reverse() # 파이썬 리스트의 메소드 reverse()를 이용
        '''