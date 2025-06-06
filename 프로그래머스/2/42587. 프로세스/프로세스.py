from collections import deque

def solution(priorities, location):
    answer = 0
    count = 0
    process = deque(enumerate(priorities)) #(location, priorities)
    
    max_val = max([v[1] for v in process])
    
    while True:
        p1 = process.popleft()
        answer += 1
        if p1[1] == max_val and p1[0] == location:
            answer -= count
            break
        elif p1[1] == max_val:
            max_val = max([v[1] for v in process])
        else:
            count += 1
            process.append(p1)
            
        
    return answer