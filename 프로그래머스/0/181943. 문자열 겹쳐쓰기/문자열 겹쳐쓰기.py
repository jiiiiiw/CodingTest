def solution(my_string, overwrite_string, s):
    answer = ''
    intercept = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+intercept:]
    print(answer)
    return answer