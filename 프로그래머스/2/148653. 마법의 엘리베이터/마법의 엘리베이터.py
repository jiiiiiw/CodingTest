def solution(storey):
    answer = 0

    while storey:
        check = storey % 10
        # 6 ~ 9 을 처리할 때
        if check > 5:
            answer += (10 - check)
            storey += 10
        # 0 ~ 4 처리할 때
        elif check < 5:
            answer += check
        # 5 처리할 때
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += check
        storey //= 10

    return answer