from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        for i in logs: #이거 왜 while문으로 하면 에러??
            if i[0][0] == "d":
                digit.append(i)
            else: letter.append(i)

        print("digit", digit)
        print("letter", letter)


sol = Solution()
sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

list = [1,2,3,4]
list.sort()
print(list)
print(list.sort())