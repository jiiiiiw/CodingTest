def solution(str1, str2):
    answer = ''
    standard = len(str1)
    for i in range(2*standard):
        if i % 2 == 0:
            answer += str1[int(i/2)]
        else:
            answer += str2[int(i/2 - 1/2)]
    print(answer)
    return answer