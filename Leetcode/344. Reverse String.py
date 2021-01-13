class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        time = len(s)/2
        count = 0
        while time >= 1 :
            time -= 1
            temp = s[count]
            s[count] = s[-(count+1)]
            s[-(count+1)] = temp
            count += 1