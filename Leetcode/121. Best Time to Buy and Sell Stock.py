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
