from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    returnlist = [i,j]
                    returnlist.sort()
                    return returnlist
                j += 1

'''
newnums = []
for i in nums:
    if i < target:
        newnums.append(i)

print(newnums)
for i in range(len(newnums)):
    for j in range(len(newnums)-1):
        j += 1
        print(i,j)
        if newnums[i] + newnums[j] == target:
            print(newnums[i]+newnums[j])
            returnlist = [i,j]
            returnlist.sort()
            return returnlist

잘못생각한 점, 헷갈렸던 점    
1. nuwnums를 하면 순서가 달라짐.
   여기서 원하는 것은 정답이 되는 "숫자"가 아닌 "순서"이기 때문에 정답 또한 달라짐   
2. 이중 for문에 집착함.
   j는 무조건 i보다 뒤에서부터 시작해야하는데, 이중 for문에 집착해서 해결법을 찾는데 오래걸림.
3. for i in range보다 for i in newnums를 쓰고 싶었음.
   -> 해결 방안 찾아보자,,     
'''