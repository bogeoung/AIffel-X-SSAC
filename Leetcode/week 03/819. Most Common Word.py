from typing import *
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]
        '''
        리스트 컨프리헨션의 조건절
        "식 for 변수 in 리스트 if 조건식"
        if는 for 문 다음에 위치해야함.
        word / for word in re.sub().lower().split() / if 문으로 생각하면 되려나?
        1. paragraph에서 단어 문자(\w)가 아닌(^)것을 빼고
        2. 소문자로 바꾼 다음에
        3. split으로 뗀 word 중
        4. word가 banned 안에 없는 것들로
        5. words 리스트를 생성함. 
        
        참고 : https://dojang.io/mod/page/view.php?id=2285
        '''

        count = {}
        for word in words:
            if word in count.keys():
                count[word] += 1
            else:
                count[word] = 1

        return(max(count, key = lambda x : count[x]))
        # 가장 count가 큰 key를 리턴함.
        # 참고 : https://jaeworld.github.io/2018-09-06/python_lambda_usage


test = Solution()
print(test.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))