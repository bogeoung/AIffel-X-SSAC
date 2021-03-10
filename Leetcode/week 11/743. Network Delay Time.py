from typing import List
import collections

# 못품
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        Q = [(0,)]
        while Q:


test = Solution()
test.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)