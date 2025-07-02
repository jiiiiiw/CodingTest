from collections import deque

def solution(r, cx, cy, ix, iy):
    board = [[0] * 102 for _ in range(102)]
    
    for a, b, c, d in r:
        a, b, c, d = a*2, b*2, c*2, d*2
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                if i == a or i == c or j == b or j == d:
                    if board[i][j] != 2:
                        board[i][j] = 1
                else:
                    board[i][j] = 2
    
    q = deque()
    v = [[0] * 102 for _ in range(102)]
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    
    sx, sy = cx * 2, cy * 2
    ex, ey = ix * 2, iy * 2
    
    q.append((sx, sy, 0))
    v[sx][sy] = 1
    
    while q:
        x, y, cnt = q.popleft()
        if x == ex and y == ey:
            return cnt // 2 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if not v[nx][ny] and board[nx][ny] == 1:
                    v[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))
