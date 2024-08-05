# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 progresses
# 각 작업의 개발 속도가 적힌 speeds

def solution(progresses, speeds):
    answer = []
    while progresses: # 매일 개발 속도 만큼 작업 진도가 올라감
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            counter = 0
        while progresses and 100 <= progresses[0]:
            counter += 1
            del progresses[0]
            del speeds[0]
        if counter:
            answer.append(counter)
            
    return answer
    
    return answer