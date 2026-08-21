class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() for i in s if i.isalnum())
        l = len(s)
        for i in range(l//2):
            if s[i]!=s[l-i-1]:
                return False
        return True
