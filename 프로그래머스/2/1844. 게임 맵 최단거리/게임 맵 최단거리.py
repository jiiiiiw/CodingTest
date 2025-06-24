from collections import deque

def solution(m):
    n, k = len(m), len(m[0])
    v = [[0]*k for _ in range(n)]
    q = deque()
    q.append((0, 0))
    v[0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < n and 0 <= b < k and m[a][b] == 1 and v[a][b] == 0:
                v[a][b] = v[x][y] + 1
                q.append((a, b))

    return v[n-1][k-1] if v[n-1][k-1] != 0 else -1