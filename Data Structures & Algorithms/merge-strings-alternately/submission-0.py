class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        l1 = len(word1)
        l2 = len(word2)
        i, j = 0, 0
        while i<l1 and j<l2:
            s.append(word1[i])
            s.append(word2[j])
            i+=1
            j+=1
        if i==l1:
            s.append(word2[j:])
        else:
            s.append(word1[i:])
        return ''.join(s)
        