from collections import Counter

def solution(weights):
    answer = 0
    
    # 1:1
    counter = Counter(weights)
    for key,value in counter.items():
        if value>=2:
            answer+= value *(value-1)//2 # 일종의 조합
            
    weights = set(weights) #1:1 구한 후 중복 제거  
    
    #2:3, 2:4, 3:4 각각의 경우를 생각해보자
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w] # 경우의 수 구하기
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    return answer