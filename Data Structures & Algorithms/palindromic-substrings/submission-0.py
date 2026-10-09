class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [0]*len(s)
        for i in range(len(s)):
            x, y = i, i
            while x>=0 and y<len(s) and s[x]==s[y]:
                x-=1
                y+=1
                dp[i]+=1
            x, y = i, i+1
            while x>=0 and y<len(s) and s[x]==s[y]:
                x-=1
                y+=1
                dp[i]+=1
        return sum(dp)