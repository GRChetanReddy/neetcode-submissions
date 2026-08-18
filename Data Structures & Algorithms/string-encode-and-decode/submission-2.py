class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for i in range(len(strs)):
            l = str(len(strs[i])).zfill(3)
            s.append('#*' + l + strs[i])
        return ''.join(s)

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i<len(s):
            if s[i:i+2]=='#*':
                k = int(s[i+2:i+5])
                strs.append(s[i+5:i+k+5])
                i = i + k + 5
        return strs


