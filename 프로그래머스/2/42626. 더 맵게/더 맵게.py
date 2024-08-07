import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # heap 자료구조로 변경
    # print(scoville)
    cnt = 0 # 섞는 횟수 초기화
    
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        low1 = heapq.heappop(scoville)
        
        if low1 < K:
            low2 = heapq.heappop(scoville)
            new = low1 + (low2 * 2)
            heapq.heappush(scoville, new)
            cnt += 1
        else:
            return cnt
        