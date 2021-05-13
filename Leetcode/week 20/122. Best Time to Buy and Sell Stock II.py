class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        풀이 1
        result = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result
        '''

        # 풀이 2 , 0과 비교해서 양수인 경우 더함
        return sum(max(prices[i+1] - prices[i],0) for i in range(len(prices)-1))