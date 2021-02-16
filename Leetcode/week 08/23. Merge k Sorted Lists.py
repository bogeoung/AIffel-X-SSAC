# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        # heapq 모듈에는 파이썬의 보통 리스트를 마치 최소힙처럼 다룰 수 있게 해줌.
        # 따라서 빈 리스트 생성 후, heapq 모듈의 함수를 호출할 때마다 이 리스트를 인자로 넘겨야 함.
        heap = []

        # input : [[1,4,5],[1,3,4],[2,6]]
        # heapq 모듈은 최소 힙을 지원. 따라서 list.val이 작은 순서대로 pop()할 수 있음.
        for i in range(len(lists)):  # len(lists) = 3
            if lists[i]: # [1,4,5]와 같이 lists내 list를 순차적으로 뽑음
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                # heapq.heappush(원소를 추가할 대상리스트, 추가할 원소)가 원래 공식
                # 하지만 그런 경우 중복된 값에 있어서 오류가 발생하기 때문에 연결리스트의 순서를 나타내는 i를 추가함.

        while heap:
            node = heapq.heappop(heap)
            # heapq.heappop(원소를 삭제할 대상 리스트) 수행시, 가장 작은 원소를 삭제 후 그 값을 리턴
            #print("---")
            #print(node)
            idx = node[1]
            # 가장 작은 원소를 리턴한 ListNode의 next를 뽑음
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

# 참고 : https://www.daleseo.com/python-heapq/
