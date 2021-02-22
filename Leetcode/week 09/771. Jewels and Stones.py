class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {} # 가지고 있는 stone을 종류별로 몇개 가지고 있는지 저장할 딕셔너리 선언
        count = 0 # 총 보석 수를 저장할 변수 선언 및 초기화

        for char in stones:
            if char not in freqs: #char가 freq 딕셔너리에 존재하지 않는 키이면, 값을 1로 딕셔너리에 추가
                freqs[char] = 1
            else:                 #char가 freq 딕셔너리에 이미 존재하는 키라면, 값에 1 추가
                freqs[char] += 1

        for char in jewels:
            if char in freqs:     # 보석이 freq 딕셔너리에 존재한다면, 해당 키의 값을 가져와 count에 더함.
                count += freqs[char]

        return count

    '''
    My Code
    try 1
    1. stones를 enumerate를 수행 -> 대소문자 구분 필요
    2. enumerate 객체를 해시 테이블로 저장
    3. j 길이만큼 반복 & 해시 테이블에서 값 빼내서 합산
    -> 실패. enumerate 를 수행하면, {0: 'a', 1: 'A', 2: 'A', 3: 'b', 4: 'b', 5: 'b', 6: 'b'}이런 형태로 나옴.
    그 때 개수 세는데 사용했던 메소드가 enumerate가 아닌가..?? 흠 -> counter였나봄.

    try 2
    1. enumerate 대신 count 사용하기
    '''
        # hashmap = dict()
        # total_count = 0
        #
        # for i in stones:
        #     hashmap[i] = stones.count(i)
        #
        # for i in jewels:
        #     if i in hashmap:
        #         total_count += hashmap[i]
        #
        # print(total_count)
        # return total_count

num = Solution()
num.numJewelsInStones("z", "ZZ")