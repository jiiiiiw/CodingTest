def solution(progresses, speeds):
    answer = []
    restJob = []
    
    for p, s in zip(progresses, speeds):
        newP = 100 - p
        if newP % s == 0: restJob.append(newP // s)
        else: restJob.append((newP // s) + 1)
        
    restJob.reverse()
    
    top = restJob[-1]
    restJob.pop()
    answer.append(1)
    
    while restJob:
        j = restJob.pop()
        if j <= top: answer[-1] += 1
        else: 
            answer.append(1)
            top = j
    
    return answer