def solution(t):
    t.sort()
    v = [0] * len(t)
    r = []

    def dfs(p, path, d):
        if d == len(t):
            r.append(path[:])
            return
        for i in range(len(t)):
            if not v[i] and t[i][0] == p:
                v[i] = 1
                dfs(t[i][1], path + [t[i][1]], d + 1)
                v[i] = 0

    dfs("ICN", ["ICN"], 0)
    return r[0]