def solution(n, c):
    c.sort(key=lambda x: x[2]) 
    p = [i for i in range(n)]   

    def f(x):
        if p[x] != x:
            p[x] = f(p[x])
        return p[x]

    def u(x, y):
        x = f(x)
        y = f(y)
        if x != y:
            p[y] = x
            return True
        return False

    a = 0 
    for x, y, z in c:
        if u(x, y):
            a += z

    return a
