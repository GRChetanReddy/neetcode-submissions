class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        max_l = [0]
        max_r = [0]
        l, r, w = 0, 0, 0
        for i in range(1, h):
            l = max(l, height[i-1])
            max_l.append(l)
        for i in range(h-2, -1, -1):
            r = max(height[i+1], r)
            max_r.append(r)
        for i in range(h):
            wtr = min(max_l[i], max_r[h-i-1]) - height[i]
            if wtr>=0:
                w+=wtr
        return w

        