def solution(targets):
    # 1. 구간을 끝점(e)을 기준으로 오름차순 정렬
    targets.sort(key=lambda x: x[1])
    
    # 2. 첫 번째 구간의 끝점에 미사일 발사
    missiles = 0
    last_missile_position = -float('inf')
    
    for target in targets:
        s, e = target
        
        # 현재 발사 위치가 해당 구간을 커버하지 못하면 새로운 미사일 발사
        if last_missile_position < s:
            last_missile_position = e - 0.0001  # e보다 조금 작은 실수 위치에 발사
            missiles += 1
    
    return missiles
