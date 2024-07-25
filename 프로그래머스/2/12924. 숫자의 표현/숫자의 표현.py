def solution(n): # 더블 포인터를 사용해보자
    answer = 0
    front, total, back = 1, 1, 2
    while front < back:
        if total < n:
            total += back
            back += 1
        elif n < total:
            total -= front
            front += 1
        else:
            answer += 1
            total -= front
            front += 1
    return answer
    