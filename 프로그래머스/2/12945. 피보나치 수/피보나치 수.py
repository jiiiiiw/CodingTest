def solution(n):
    save = [0 for __ in range(n + 1)]
    save[1] = 1
    for idx in range(2, n+1):
        save[idx] = save[idx-1] + save[idx-2]
    return save[n] % 1234567
    