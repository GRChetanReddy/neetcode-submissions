from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dq = deque()
        t = 0
        f = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    dq.append((i, j))
                elif grid[i][j]==1:
                    f+=1
        while dq and f>0:
            l = len(dq)
            for _ in range(l):
                i, j = dq.popleft()
                for di, dj in dr:
                    ni, nj = i+di, j+dj
                    if 0<=ni and ni<n and 0<=nj and nj<m:
                        if grid[ni][nj]==1:
                            grid[ni][nj]=2
                            dq.append((ni, nj))
                            f-=1
                        
            t+=1
            
        return -1 if f!=0 else t
