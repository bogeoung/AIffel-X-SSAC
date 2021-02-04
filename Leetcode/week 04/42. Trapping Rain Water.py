from typing import *
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <1:
            return 0

        max_height = max(height)
        max_height_index = height.index(max_height)
        max_size = max_height * len(height)

        tlist_1 = height[:max_height_index]
        tlist_2 = height[max_height_index + 1:]

        temp = 0
        for i in tlist_1:
            if i > temp:
                temp = i
            max_size = max_size - (max_height - temp)
        print("왼쪽 다 했을 때 max_size", max_size)

        count = 0
        if max_height_index != len(height):
            temp = height[max_height_index + 1]
            for i in tlist_2:
                count += 1
                if i < temp and count == len(tlist_2):
                    return max_size - temp - sum(height)
                max_size = max_size - (max_height - temp)
            print("오른쪽 다 했을 때 max_size", max_size)

        return max_size - sum(height)


test = Solution()
print(test.trap(height = [4,2,0,3,2,5]))
'''
                if len(height) <1:
            return 0
        max_height = max(height)
        max_height_index = height.index(max_height)
        max_size = max_height * len(height)

        temp = 0
        for i in height:
            if i > temp:
                temp = i
            if i == max_height:
                if height.index(i) == len(height)-1:
                    return max_size - sum(height)
                else:
                    max_size = max_size - (max_height - temp)
                    temp = height[max_height_index + 1]
                    continue
            max_size = max_size - (max_height - temp)

        max_size = max_size - sum(height)
        return max_size
'''
'''
        max_height = max(height)
        max_height_index = height.index(max_height)
        print(max_height_index)
        max_size = max_height * len(height)

        tlist_1 = height[:max_height_index]
        tlist_2 = height[max_height_index+1:]

        temp = 0
        for i in tlist_1:
            if i > temp:
                temp = i
            max_size = max_size - (max_height - temp)
        print("왼쪽 다 했을 때 max_size", max_size)

        if max_height_index != len(height):
            temp = height[max_height_index + 1]
            for i in tlist_2:
                if i > temp:
                    temp = i
                max_size = max_size - (max_height - temp)
            print("오른쪽 다 했을 때 max_size", max_size)

        return max_size - sum(height)
'''