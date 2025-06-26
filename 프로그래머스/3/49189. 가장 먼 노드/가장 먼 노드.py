from collections import deque, defaultdict

def solution(n, v):
    g = defaultdict(list)
    for a, b in v:
        g[a].append(b)
        g[b].append(a)

    d = [-1] * (n + 1)
    d[1] = 0

    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if d[nxt] == -1:
                d[nxt] = d[cur] + 1
                q.append(nxt)

    max_d = max(d)
    return d.count(max_d)