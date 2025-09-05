def solution(N, stations, W):
    cover = 2 * W + 1         
    need = 0
    start = 1                  

    for s in stations:
        left = s - W          
        if left > start:       
            length = left - start
            need += (length + cover - 1) // cover  # 올림 나눗셈
      
        start = max(start, s + W + 1)

    if start <= N:
        length = N - start + 1
        need += (length + cover - 1) // cover

    return need
