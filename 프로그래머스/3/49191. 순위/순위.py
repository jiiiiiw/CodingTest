def solution(n, r):
    g = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in r:
        g[a][b] = 1   
        g[b][a] = -1  

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if g[i][k] == 1 and g[k][j] == 1:
                    g[i][j] = 1
                    g[j][i] = -1
                if g[i][k] == -1 and g[k][j] == -1:
                    g[i][j] = -1
                    g[j][i] = 1

    cnt = 0
    for i in range(1, n + 1):
        c = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            if g[i][j] != 0:
                c += 1
        if c == n - 1:
            cnt += 1
    return cnt