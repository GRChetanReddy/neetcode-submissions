class Solution:
    def longestPalindrome(self, s: str) -> str:
        resR, resL = 0, 0
        for i in range(len(s)):
            x, y = i, i
            while x>=0 and y<len(s) and s[x]==s[y]:
                x-=1
                y+=1
            if y-x-1>resR-resL:
                resR = y
                resL = x+1
            x, y = i, i+1
            while x>=0 and y<len(s) and  s[x]==s[y]:
                x-=1
                y+=1
            if y-x-1>resR-resL:
                resR = y
                resL = x+1
        return s[resL:resR]  