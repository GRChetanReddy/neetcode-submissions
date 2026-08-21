class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum())
        l, r = 0, len(s)-1

        def compare(l, r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
            
        while l<=r:
            if s[l]!=s[r]:
                if compare(l+1, r):
                    return True
                elif compare(l, r-1):
                    return True
                return False
            l+=1
            r-=1                
        return True
        