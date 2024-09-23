from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    # 1. info를 기반으로 가능한 모든 조합의 dict를 만든다.
    info_dict = defaultdict(list)
    
    for i in info:
        data = i.split()
        conditions = data[:-1]
        score = int(data[-1])
        
        # 가능한 모든 조합을 만들고, 해당 조합에 score를 추가
        for n in range(5):
            combi = list(combinations([0, 1, 2, 3], n))
            for c in combi:
                temp_conditions = conditions[:]
                for idx in c:
                    temp_conditions[idx] = '-'
                key = ' '.join(temp_conditions)
                info_dict[key].append(score)
    
    # 2. 각 조합에 해당하는 점수 리스트를 오름차순 정렬
    for key in info_dict:
        info_dict[key].sort()
    
    # 3. query를 처리하여 결과를 구함
    answer = []
    for q in query:
        q = q.replace(" and ", " ")
        q_data = q.split()
        q_conditions = ' '.join(q_data[:-1])
        q_score = int(q_data[-1])
        
        if q_conditions in info_dict:
            scores = info_dict[q_conditions]
            
            # 이분탐색으로 해당 점수 이상인 지원자 수 찾기
            idx = bisect.bisect_left(scores, q_score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    
    return answer