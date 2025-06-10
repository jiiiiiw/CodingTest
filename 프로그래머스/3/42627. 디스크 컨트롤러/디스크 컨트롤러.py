import heapq

def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)
    heap = []
    jobs.sort()
    
    while True:
        new_jobs = []
        for j in jobs:
            if j[0] <= time:
                heapq.heappush(heap, (j[1], j))
            else:
                new_jobs.append(j)
        jobs = new_jobs
        
        if not heap:
            if not jobs:
                break
            else:
                time += 1
        else:
            _, actual = heapq.heappop(heap)
            answer += (time + actual[1]-actual[0])
            time += actual[1]    
            
    return answer // n