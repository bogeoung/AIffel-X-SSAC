from typing import *
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]

        count = {}
        for word in words:
            if word in count.keys():
                count[word] +=1
            else:
                count[word] = 1

        return(max(count, key = ))
