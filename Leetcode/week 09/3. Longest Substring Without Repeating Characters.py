class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        count = 0
        
        # try 1
        # 앞에 연속적인 문자가 나온 경우 찾지를 못함.
        # for char in s:
        #     if char not in hashmap:
        #         count += 1
        #         hashmap[char] = 0
        #     else:
        #         count = 0
        #         hashmap = {}
                
        # try 2


        print(count)
        return count
    
num = Solution()
num.lengthOfLongestSubstring("abcabcbb")