def time_to_minutes(time):
    # "hh:mm" 형식을 분 단위로 변환
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(plans):
    # 1. 시작 시간을 기준으로 정렬
    plans = sorted(plans, key=lambda x: time_to_minutes(x[1]))

    result = []  # 과제를 끝낸 순서대로 담을 리스트
    stack = []   # 진행 중이던 과제를 임시로 보관할 스택
    current_time = 0  # 현재 시간(분 단위)

    for i in range(len(plans)):
        name, start, playtime = plans[i]
        start_time = time_to_minutes(start)
        playtime = int(playtime)

        # 현재 과제 시작 전까지의 시간을 처리
        while stack and current_time < start_time:
            prev_name, remaining_time = stack.pop()
            # 멈춰둔 과제를 남은 시간 동안 진행
            if current_time + remaining_time <= start_time:
                # 과제가 완료되면 결과에 추가
                current_time += remaining_time
                result.append(prev_name)
            else:
                # 아직 끝나지 않았다면, 남은 시간 업데이트 후 스택에 다시 넣음
                stack.append((prev_name, remaining_time - (start_time - current_time)))
                current_time = start_time
                break

        # 새 과제 시작
        current_time = start_time
        stack.append((name, playtime))

    # 남은 과제들 처리
    while stack:
        name, remaining_time = stack.pop()
        result.append(name)

    return result
