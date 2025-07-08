from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def fnd(b, v):
    res = []
    vis = [[0]*len(b) for _ in range(len(b))]

    for i in range(len(b)):
        for j in range(len(b)):
            if not vis[i][j] and b[i][j] == v:
                q = deque([(i, j)])
                b[i][j] = v ^ 1
                vis[i][j] = 1
                tmp = [(i, j)]

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < len(b) and 0 <= ny < len(b) and b[nx][ny] == v:
                            q.append((nx, ny))
                            b[nx][ny] = v ^ 1
                            vis[nx][ny] = 1
                            tmp.append((nx, ny))
                res.append(tmp)
    return res

def to_map(a):
    x, y = zip(*a)
    h, w = max(x)-min(x)+1, max(y)-min(y)+1
    m = [[0]*w for _ in range(h)]
    for i, j in a:
        m[i-min(x)][j-min(y)] = 1
    return m

def rot(p):
    h, w = len(p), len(p[0])
    r = [[0]*h for _ in range(w)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if p[i][j]: cnt += 1
            r[j][h-1-i] = p[i][j]
    return r, cnt

def solution(g, t):
    ans = 0
    e = fnd(g, 0) 
    pz = fnd(t, 1)  

    for a in e:
        done = 0
        tm = to_map(a)

        for b in pz:
            if done: break
            pm = to_map(b)

            for _ in range(4):
                pm, cnt = rot(pm)
                if pm == tm:
                    ans += cnt
                    pz.remove(b)
                    done = 1
                    break
    return ans