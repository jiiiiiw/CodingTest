def solution(r):
    r.sort(key=lambda x: x[1])  
    c = -30001 
    a = 0  

    for s, e in r:
        if s > c:  
            c = e
            a += 1

    return a