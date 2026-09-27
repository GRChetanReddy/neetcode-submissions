class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        def bfs(i, j):
            a = 1
            q = deque()
            q.append((i, j))
            vis.add((i, j))
            while q:
                i, j = q.popleft()
                for di, dj in dr:
                    ni = di + i
                    nj = dj + j
                    if 0<=ni and ni<n and 0<=nj and nj<m:
                        if (ni, nj) not in vis and grid[ni][nj]==1:
                            q.append((ni, nj))
                            vis.add((ni, nj))
                            a+=1
                        
            return a

        ma = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (i, j) not in vis:
                    ma = max(ma, bfs(i, j))
        return ma