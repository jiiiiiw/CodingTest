import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0  

    heap = [-w for w in works]  
    heapq.heapify(heap)

    for _ in range(n):
        max_work = heapq.heappop(heap)
        heapq.heappush(heap, max_work + 1) 

    return sum(w ** 2 for w in heap)
