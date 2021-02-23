from collections import Counter
from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_list = Counter(nums)
        return_list = []

        for i in num_list:
            if num_list[i] >= k:
                return_list.append(i)

        return return_list

test = Solution()
print(test.topKFrequent([1,2], 2))
# 이 코드가 왜 틀린지 이해를 못하겠네...
# input이 [1,2], k=2이면 output으로 []가 맞는거 아닌가???
# 왜 output이 [1,2]인지 몰라서 수정을 못하겠음.