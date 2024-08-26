# 하나하나 세는 방법보다는 다른 방법으로
# 등장횟수를 세어보자
# 조합을 사용해보자
import itertools

def solution(orders, course):
    
    table = {}
    for i in course:
        table[i] = {} # 각각에 모두 딕셔너리가 존재
    for s in orders:
        for i in course:
            for comb in itertools.combinations(s, i):
                menu = "".join(sorted(comb))
                if menu not in table[i].keys():
                    table[i][menu] = 1
                else:
                    table[i][menu] += 1
            
    answer = []
    for i in course:
        if len(table[i]) == 0:
            continue
        big = max(table[i].values())
        if big < 2:
            continue
        for key in table[i].keys():
            if big == table[i][key]:
                answer.append(key)
    print(answer)
    return sorted(answer)