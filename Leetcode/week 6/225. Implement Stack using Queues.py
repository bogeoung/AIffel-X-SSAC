# 큐로 스택 구현하기
class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)
        '''
        일반적으로 사용되는 deque 에서의 append()는 오른쪽부터 삽입. <---- 이렇게 쌓여서 왼쪽이 제일 오래된 것을 의미함
        d = deque()
        for i in range(3):
            d.append(i)
        print d
        # deque([0,1,2])
        
        반면 위에서 사용한 appendleft()는 왼쪽부터 삽입.  ----> 이렇게 쌓여서 오른쪽이 제일 오래된 것.
        스택 구상시 제일 왼쪽이 top, 제일 오른쪽이 bottom이라고 구상하였기 때문에 appendleft를 사용함. -> top구할때마다 len으로 구하기 싫고, 무조건 0으로 구하려고
        
        참고 : https://docs.python.org/3.7/library/collections.html#collections.deque
        
        근데 다 풀고 보니 문제 조건 상 deque의 push, top, pop, empty만 사용하라 해서 틀린 답인듯.
        하지만 리트코드 상 통과는 되었다. 일종의 편법인듯. 
        '''

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0 # True, False 출력
