def solution(x):
    answer = True
    sum_x = 0
    str_x = str(x)
    for elem in str_x:
        sum_x += int(elem)

    if x % sum_x:
        answer = False

    return answer