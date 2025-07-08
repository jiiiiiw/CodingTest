def solution(n, k):
    r = []
    for d in n:
        while k > 0 and r and r[-1] < d:
            r.pop()
            k -= 1
        r.append(d)
    return ''.join(r[:len(n)-k])
