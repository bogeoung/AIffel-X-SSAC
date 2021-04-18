class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,  # 콤마 연산자를 통해 중첩 리스트로 만듬.
        return merged

'''
intervals = [[1,3],[2,6],[8,10],[15,18]
merged = [[1,6],[8,10],[15,18]]
'''
