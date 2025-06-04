def solution(genres, plays):
    answer = []
    dic = {}
    flag = 0
    
    for g, p in zip(genres, plays):
        if g in dic: dic[g].append([p, flag])
        else: dic[g] = [[p, flag]]
        flag += 1
    
    for k in dic:
        dic[k].sort(key = lambda x: (-x[0], x[1]))
        
    arr = [[k, sum([x[0] for x in v])] for k, v in dic.items()]
    arr.sort(key = lambda x: x[1], reverse = True)
    
    for a in arr:
        if len(dic[a[0]]) == 1: answer.append(dic[a[0]][0][1])
        else: 
            answer.append(dic[a[0]][0][1])
            answer.append(dic[a[0]][1][1])
    
    return answer