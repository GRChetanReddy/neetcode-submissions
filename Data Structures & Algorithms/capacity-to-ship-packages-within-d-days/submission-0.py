class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calct(cap):
            t = 0 #time(in days)
            cw = 0 #current weight
            for w in weights:
                cw+=w
                if cw>cap:
                    t+=1
                    cw = w
            return t+1

        l, r = max(weights), sum(weights)
        res = 0
        while l<=r:
            k = (l+r)//2
            if calct(k)<=days:
                r = k-1
                res = k
            else:
                l = k+1
        return res

        