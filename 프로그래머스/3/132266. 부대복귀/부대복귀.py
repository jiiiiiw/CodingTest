from collections import deque, defaultdict

def solution(n, r, s, d):  # n: 지역 수, r: 길 정보, s: 서로다른지역, d: 강철부대지역
    g = defaultdict(list)
    for a, b in r:
        g[a].append(b)
        g[b].append(a)

    dist = [-1] * (n + 1)
    q = deque()
    q.append(d)
    dist[d] = 0

    while q:
        x = q.popleft()
        for nx in g[x]:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

    return [dist[x] for x in s]