def solution(keymap, targets):
    t = ""
    for i in targets :
        t += i
    t = list(set(t))
    
    d = dict()
    for i in t :
        temp = [j.index(i) for j in keymap if i in j]
        if len(temp) == 0 :
            d[i] = -1
        else :
            d[i] = min(temp) + 1
            
    result = list()
    for j in targets :
        temp = [d[i] for i in j]
        if -1 in temp :
            result.append(-1)
        else :
            result.append(sum(temp))
            
    return result