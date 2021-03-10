import heapq
import collections
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 각 노드에 연결되어 있는 항공편을 구성함
        # defaultdict(<class 'list'>, {0: [(1, 100), (2, 500)], 1: [(2, 100)]})
        for u,v,w in flights:
            graph[u].append((v,w))

        # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수))
        Q = [(0,src,K)]

        while Q :
            price, node, k = heapq.heappop(Q) #heapq모듈은 파이썬의 보통 리스트를 최소 힙처럼 다룰 수 있도록 해줌.
            if node == dst:                   #참고 : https://www.daleseo.com/python-heapq/
                return price
            if k >= 0:
                for v,w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt,v,k-1))
                    #heappush(원소를 추가할 대상 리스트, 추가할 원소)
                    #파이썬이 제공하는 힙은 최소 힙으로, price가 낮은 순으로 정렬이 됨.
        # 경로가 존재하지 않을 경우
        return -1

'''
문제설명
n개의 도시들은 m flight를 통해 연결되어 있음
각각의 flight는 [u,v,w]로 구성되어 있으며, u는 출발지 v는 도착지 w는 비용임.
모든 도시, 비행편이 제공되었을 때 src에서 출발하여 dst까지 도착하는 가장 싼 가격을 찾되, 
k경유지 이내에 도착해야함.
경로가 존재하지 않을 경우 -1을 리턴
'''

temp = Solution()
print(temp.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
