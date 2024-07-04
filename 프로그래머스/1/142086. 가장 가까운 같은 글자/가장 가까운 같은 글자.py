def solution(s):
    answer = []
    s = list(s)
    for i in range(len(s)):
        if s[i] in s[:i]:
            answer.append(i-s.index(s[i]))
            s[s.index(s[i])] = '0'
        else:
            answer.append(-1)
    return answer