def solution(priorities, location):
    queue = [(p, i) for i, p in enumerate(priorities)]
    count = 0
    
    while queue:
        # 현재 프로세스를 큐에서 꺼냄
        current = queue.pop(0)
        
        # 큐에 남아있는 프로세스 중 우선순위가 더 높은 것이 있는지 확인
        if any(current[0] < q[0] for q in queue):
            # 있다면 현재 프로세스를 다시 큐의 뒤에 넣음
            queue.append(current)
        else:
            # 없다면 현재 프로세스를 실행
            count += 1
            # 현재 프로세스가 찾고있던 프로세스라면 결과 반환
            if current[1] == location:
                return count