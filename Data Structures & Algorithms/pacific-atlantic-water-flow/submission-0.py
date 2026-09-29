from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(heights)
        m = len(heights[0])
        dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        a = set()
        aq = deque()
        p = set()
        pq = deque()
        for i in range(n):
            p.add((i, 0))
            pq.append((i, 0))
            a.add((i, m-1))
            aq.append((i, m-1))
        for i in range(m):
            p.add((0, i))
            pq.append((0, i))
            a.add((n-1, i))
            aq.append((n-1, i))

        while aq:
            i, j = aq.popleft()
            for di, dj in dr:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<m and (ni, nj) not in a:
                    if heights[ni][nj]>=heights[i][j]:
                        aq.append((ni, nj))
                        a.add((ni, nj))
        
        while pq:
            i, j = pq.popleft()
            for di, dj in dr:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<m and (ni, nj) not in p:
                    if heights[ni][nj]>=heights[i][j]:
                        pq.append((ni, nj))
                        p.add((ni, nj))

        for i, j in a:
            if (i, j) in p:
                res.append([i, j])

        return res

        