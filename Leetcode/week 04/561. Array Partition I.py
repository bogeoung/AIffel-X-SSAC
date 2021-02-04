from typing import *
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        순서대로 나열을 해서 짝수번째 수만 더하면 됨
        '''
        nums = sorted(nums)
        i, sum = 0, 0
        print(nums)
        while i < len(nums):
            sum += nums[i]
            i += 2

        return sum
