def solution(k, d):
    count = 0
    
    # x축에 대해서 a*k 값을 계산
    for a in range(0, d + 1, k):
        # y축에 대해서 가능한 b*k의 범위 계산
        max_b = (d**2 - a**2) ** 0.5
        count += (int(max_b) // k) + 1
    
    return count
