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

'''
def maxProfit(List):
        min = 0
        max = 0
        prices = List
        for i in prices:
            if i < min :
                min = i
                max = 0
            if i > max :
                max = i
        if max - min < 0:
            result = 0
        else: result = max - min
        return result

maxProfit([1,2,3,4,5])    
'''