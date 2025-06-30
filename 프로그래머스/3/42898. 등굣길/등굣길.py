def solution(m, n, p):
    d = [[0] * m for _ in range(n)] 

    for x, y in p:
        d[y-1][x-1] = -1 

    d[0][0] = 1  

    for i in range(n):
        for j in range(m):
            if d[i][j] == -1:
                d[i][j] = 0
                continue
            if i > 0:
                d[i][j] += d[i-1][j]
            if j > 0:
                d[i][j] += d[i][j-1]
            d[i][j] %= 1000000007

    return d[n-1][m-1]