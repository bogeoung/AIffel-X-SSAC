from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index,path):
            result.append(path)

            # in range(시작숫자, 종료숫자, step)
            # 여기서는 시작숫자, 종료숫자를 지정한거라고 보면 됨.
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0,[])
        return result

temp = Solution()
print(temp.subsets([1,2,3]))