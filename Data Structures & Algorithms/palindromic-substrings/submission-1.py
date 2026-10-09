class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            x, y = i, i
            while x>=0 and y<len(s) and s[x]==s[y]:
                x-=1
                y+=1
                res+=1
            x, y = i, i+1
            while x>=0 and y<len(s) and s[x]==s[y]:
                x-=1
                y+=1
                res+=1
        return res