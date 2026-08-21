class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k = len(s)//2
        l = len(s)-1
        for i in range(k):
            s[i], s[l-i] = s[l-i], s[i]
        return 