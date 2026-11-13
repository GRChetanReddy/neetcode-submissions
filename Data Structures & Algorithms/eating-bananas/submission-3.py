import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pl = len(piles)
        if pl==1:
            return math.ceil(piles[0]/h)
        def findt(r):
            t = 0
            for i in range(pl):
                t+=math.ceil(piles[i]/r)
            return t

        res = 0
        l, r = 1, max(piles)
        while l<=r:
            m = (l+r)//2
            if findt(m)>h:
                l = m+1
            else:
                r = m-1
                res = m
        return res