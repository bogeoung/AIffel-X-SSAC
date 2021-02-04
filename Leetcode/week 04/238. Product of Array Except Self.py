from typing import *
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1
        for i in range(0,len(nums)):
            result.append(p)
            p = p*nums[i]
        p = 1
        for i in range(len(nums) -1, 0 -1, -1):
            result[i] = result[i] * p
            p = p*nums[i]

        return result

test = Solution()
print(test.productExceptSelf([1,2,3,4]))
'''
내가 한 풀이 -> time exceed나옴 
        result = []

        for i in range(len(nums)):
            print(i)
            k, j = 0, len(nums) - 1
            left, right = 1, 1
            while k >= 0 and k < i:
                left = left * nums[k]
                k = k+1
            while j > i and j < len(nums):
                right = right * nums[j]
                j = j-1
            result.append(left*right)
            i += 1
        return result
'''