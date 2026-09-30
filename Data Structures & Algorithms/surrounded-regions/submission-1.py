from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis = set()
        dq = deque()
        dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(board)
        m = len(board[0])
        for i in range(n):
            if board[i][0]=='O':
                dq.append((i, 0))
                vis.add((i, 0))
            if board[i][m-1]=='O':
                dq.append((i, m-1))
                vis.add((i, m-1))
        for i in range(m):
            if board[0][i]=='O':
                dq.append((0, i))
                vis.add((0, i))
            if board[n-1][i]=='O':
                dq.append((n-1, i))
                vis.add((n-1, i))
        while dq:
            i, j = dq.popleft()
            for di, dj in dr:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<m and (ni, nj) not in vis:
                    if board[ni][nj]=='O':
                        dq.append((ni, nj))
                        vis.add((ni, nj))
        
        for i in range(n):
            for j in range(m):
                if board[i][j]!='X' and (i, j) not in vis:
                    board[i][j]='X'

            

