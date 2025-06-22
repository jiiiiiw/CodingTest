def solution(w):
    a = ['A', 'E', 'I', 'O', 'U']
    p = [781, 156, 31, 6, 1]  # 자리별 가중치

    r = 0
    for i, c in enumerate(w):
        r += a.index(c) * p[i] + 1
    return r
