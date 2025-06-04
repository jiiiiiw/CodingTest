def solution(clothes):
    dic = {}
    
    for c in clothes:
        if c[1] in dic : dic[c[1]] += 1
        else: dic[c[1]] = 1
    print(dic)
        
    temp = 1
    
    for key in dic:
        temp *= (dic[key] + 1)
    
    return temp - 1