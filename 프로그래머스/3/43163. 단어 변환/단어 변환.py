from collections import deque

def solution(b, t, w):
    if t not in w:
        return 0
    
    q = deque()
    q.append((b, 0))  

    def can_convert(a, b):
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
        return c == 1

    v = set() 

    while q:
        x, d = q.popleft()
        if x == t:
            return d
        for nx in w:
            if nx not in v and can_convert(x, nx):
                v.add(nx)
                q.append((nx, d + 1))

    return 0