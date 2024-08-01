def solution(n):
    # 거꾸로 생각해보자
    answer = 0
    while n:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            answer += 1
    return answer