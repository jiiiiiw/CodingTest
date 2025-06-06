def solution(string):
    answer = True
    tmp = []
    
    for s in string:
        if not tmp:
            if s == ')': answer = False
            else: tmp.append(s)
        else:
            if s == ')': tmp.pop()
            else: tmp.append(s)
    
    if tmp: answer = False
    return answer