class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dct:
            self.dct[key].append([timestamp, value])
        else:
            self.dct[key] = [[timestamp, value]]        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dct:
            vals = self.dct[key]
            l, r = 0, len(vals)-1
            ans = ''
            while l<=r:
                k = (l+r)//2
                if vals[k][0]<timestamp:
                    l = k+1
                    ans = vals[k][1]
                elif vals[k][0]>timestamp:
                    r = k-1
                else:
                    return vals[k][1]
            return ans

        return ''