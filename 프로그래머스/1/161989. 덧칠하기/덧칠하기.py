def solution(n, m, section):
    if m == 1:
        return len(section)

    answer = 0
    i = n
    while i > 0:
        if i in section:
            answer += 1
            i -= (m - 1)
        i -= 1

    return answer