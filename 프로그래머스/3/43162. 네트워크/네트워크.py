def solution(n, c):
    v = [False] * n 

    def d(x):
        v[x] = True
        for i in range(n):
            if c[x][i] == 1 and not v[i]:
                d(i)

    a = 0  
    for i in range(n):
        if not v[i]:
            d(i)
            a += 1
    return a