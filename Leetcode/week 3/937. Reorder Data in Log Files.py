from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []

        # 구분해서 리스트 넣기
        for i in logs:
            if i.split()[1].isdigit(): #split해서 1번째 문자가 숫자이면 digit에 append -> isdigit을 사용함으로써 identifier가 달라져도 구분 가능해짐
                digits.append(i)
            else:                     #split해서 1번째 문자가 숫자가 아니면 letter에 append
                letters.append(i)

        # letters 재정렬
        '''
        sort는 정렬을 하는 리스트의 메소드인데, key옵션을 사용한 경우임.
        이 경우는 key 옵션에 지정된 함수의 결과에 따라 정렬함.
        
        파이썬의 람다 이용 "lambda 인자 : 표현식"
        첫번째 인자를 기준으로 오름차순 정렬 & 두번째 인자를 기준으로 오름차순 정렬
        
        split은 문자열을 나누는 메소드로 괄호안에 아무것도 넣어 주지 않으면 공백을 기준으로 문자열을 나눔.
        괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나눔.
        '''
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

sol = Solution()
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

'''원래 풀이
        digit = []
        letter = []
        for i in logs: #이거 왜 while문으로 하면 에러??
            if i[0][0] == "d":
                digit.append(i)
            else: letter.append(i)

        print("digit", digit)
        print("letter", letter)
<<<<<<< HEAD


sol = Solution()
sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

list = [1,2,3,4]
list.sort()
print(list)
print(list.sort())
=======
'''
>>>>>>> PC
