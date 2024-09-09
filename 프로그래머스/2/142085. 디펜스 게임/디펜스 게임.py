import heapq

def solution(n, k, enemy):
    heap = []
    for i, e in enumerate(enemy):
        # 현재 라운드의 적 수를 heap에 추가 (음수로 넣어서 최대 힙처럼 동작하게 함)
        heapq.heappush(heap, -e)
        n -= e  # 병사로 적을 막음
        
        # 병사로 다 막을 수 없는 경우
        if n < 0:
            if k > 0:  # 무적권이 남아 있으면
                n += -heapq.heappop(heap)  # 가장 큰 적 수에 무적권을 사용
                k -= 1  # 무적권 사용
            else:  # 무적권도 없으면 게임 종료
                return i  # 막은 라운드 수는 현재 라운드 번호
            
    return len(enemy)  # 끝까지 막은 경우
