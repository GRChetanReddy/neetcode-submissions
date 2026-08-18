class Solution:
    def check(self, need, window):
        for ch in need:
            if window.get(ch, 0) < need[ch]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        resl = float('inf')
        if len(s) == 1:
            if s==t:
                return s
            else:
                return ''
        if len(s) == 0:
            return ''

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        l, r = 0, 0
        res = ''
        window = {}

        while r<len(s):
            window[s[r]] = window.get(s[r], 0) + 1

            while self.check(need, window):
                if resl > r-l+1:
                    res = s[l:r+1]
                    resl = r-l+1
                window[s[l]] -= 1
                l += 1

            r+=1
        return res
        