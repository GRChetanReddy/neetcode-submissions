from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    dq.append([i, j])
                    visited.add((i, j))
        def addroom(r, c):
            if r<0 or r==m or c<0 or c==n or grid[r][c]==-1 or (r, c) in visited:
                return
            visited.add((r, c))
            dq.append([r, c])
        dist = 0
        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                grid[r][c]=dist
                for dr, dc in directions:
                    addroom(r+dr, c+dc)
                
            dist+=1
        return 

            