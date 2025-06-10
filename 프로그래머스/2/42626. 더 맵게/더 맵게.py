import heapq

def solution(scoville, K):
    answer = 0
    top = 0
    #s_heap = []
    
    heapq.heapify(scoville)
    
    for i in range(len(scoville) - 1):
        top = heapq.heappop(scoville)
        if top < K:
            answer += 1
            newS = top + 2*heapq.heappop(scoville)
            heapq.heappush(scoville, newS)
    
    if heapq.heappop(scoville) < K: answer = -1
        
    
    #while top < K:
    #    top = heapq.heappop(scoville)
    #    if top < K:
    #        answer += 1
    #        newS = top + 2*heapq.heappop(scoville)
    #        heapq.heappush(scoville, newS)
    
    return answer