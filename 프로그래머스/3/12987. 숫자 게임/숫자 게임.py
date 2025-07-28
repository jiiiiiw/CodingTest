def solution(A, B):
    from bisect import bisect_right

    B.sort()
    used = [False] * len(B)
    score = 0

    for a in A:  
        idx = bisect_right(B, a)  
        while idx < len(B) and used[idx]: 
            idx += 1
        if idx < len(B):
            used[idx] = True
            score += 1

    return score