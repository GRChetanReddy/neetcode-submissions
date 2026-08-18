class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        i = 0
        j = len(heights)-1
        while(i<j):
            w = min(heights[i],heights[j])*(j-i)
            if w>m:
                m = w
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return m
        