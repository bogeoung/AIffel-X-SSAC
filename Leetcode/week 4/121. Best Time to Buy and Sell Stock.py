from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 99999
        profit = 0
        for i in prices:
            if i < min:
                min = i
            profit = max(profit, i - min)

        return profit