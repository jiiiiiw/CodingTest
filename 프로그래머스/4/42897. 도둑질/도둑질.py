def solution(m):
    def rob(a):
        n = len(a)
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        d = [0] * n
        d[0], d[1] = a[0], max(a[0], a[1])
        for i in range(2, n):
            d[i] = max(d[i-1], d[i-2] + a[i])
        return d[-1]
    
    return max(rob(m[1:]), rob(m[:-1]))