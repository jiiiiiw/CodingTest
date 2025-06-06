def solution(progresses, speeds):
    answer = []
    restJob = []
    
    for p, s in zip(progresses, speeds):
        newP = 100 - p
        restJob.append((newP + s - 1) // s)  # 올림처리 간결하게

    for day in restJob:
        if not answer:
            answer.append(1)
            top = day
        elif day <= top:
            answer[-1] += 1
        else:
            answer.append(1)
            top = day

    return answer
