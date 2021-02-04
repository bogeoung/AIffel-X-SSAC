from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3개의 합이 0이 되는 숫자들의 쌍을 출력
        # 합이 0이 되는것이 없거나, 3개의 합이 0이 되는게 없다면 빈리스트 출력
        answer_list = []
        nums = sorted(nums)
        #추후 nums.sort()해봤으나 sorted(nums)가 더 빠름.

        # 원소의 개수가 3개 이하라면 바로 return
        if len(nums) < 3:
            return answer_list

        # 무조건 3개의 숫자를 사용해야하기 때문에 max i는 len(nums)-2임.
        for i in range(len(nums)-2):
            # 중복된 값은 계산하지 않기 위해 추가, i>0은 세 값이 모두 0인 경우에 대한 예외처리
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left, right는 i 보다 뒷항만 계산 필요해서, i가 바뀔때마다 초기화 되야함.
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else: # sum = 0인 경우
                    answer_list.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        # left<right가 무한loop를 막기위한 조건, 쓰지 않으면 runtime error 발생
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return answer_list

'''
# TRY 1 
>>> 정답은 [[-1, -1, 2], [-1, 0, 1], [-1, 1, 0], [-1, 2, -1], [0, -1, 1], 
[0, 1, -1], [1, -1, 0], [2, -4, 2], [2, -1, -1]]
중복을 제거할 방법이 필요할듯,,

        answer_list = []

        #원소의 개수가 3개 이하라면 바로 return
        if len(nums)<3:
            return answer_list

        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                print(nums[i]+nums[j])
                if 0 - (nums[i]+nums[j]) in nums:
                    k = nums.index(-(nums[i]+nums[j]))
                    answer_list.append([nums[i], nums[j], nums[k]])
                    answer_list.sort()
                j += 1
        return answer_list

test = Solution()
print("정답은", test.threeSum([-1,0,1,2,-1,-4]))
'''