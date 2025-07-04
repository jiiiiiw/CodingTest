from itertools import permutations

def solution(k, d):
    m = 0
    for p in permutations(d):
        t = k  
        c = 0  
        for a, b in p:
            if t >= a:
                t -= b
                c += 1
            else:
                break
        m = max(m, c)
    return m