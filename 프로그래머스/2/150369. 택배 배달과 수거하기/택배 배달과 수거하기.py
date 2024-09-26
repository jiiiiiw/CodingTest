def solution(cap, n, deliveries, pickups):
    total_distance = 0
    d = 0  # 배달해야 할 상자 수
    p = 0  # 수거해야 할 상자 수
    
    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            total_distance += (i + 1) * 2
    
    return total_distance