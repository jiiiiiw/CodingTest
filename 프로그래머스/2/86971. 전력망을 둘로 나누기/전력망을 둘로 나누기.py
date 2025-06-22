def solution(n, w):
    from collections import defaultdict, deque

    def b(s, g, v):
        q = deque([s])
        v[s] = True
        c = 1
        while q:
            x = q.popleft()
            for y in g[x]:
                if not v[y]:
                    v[y] = True
                    q.append(y)
                    c += 1
        return c

    m = float('inf')
    for i in range(len(w)):
        t = w[:i] + w[i+1:]
        g = defaultdict(list)
        for a, b_ in t:
            g[a].append(b_)
            g[b_].append(a)
        v = [False] * (n + 1)
        c = b(1, g, v)
        d = abs(c - (n - c))
        m = min(m, d)

    return m
