def solution(n,a,b):
    l, r = min(a, b), max(a,b)
    round = 1
    while True:
        if r % 2 == 0 and l + 1 == r:
            break
        l, r = (l + 1) // 2, (r + 1) // 2
        round += 1
    return round