def solution(k, tangerine):
    # 크기당 개수
    size_count = dict()
    for size in tangerine:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    
    #개수
    counts = sorted(size_count.values())
    
    # 가장 많은 종류부터 담아주기
    answer = 0
    while 0 < k:
        k -= counts[-1]
        del counts[-1]
        answer += 1
    return answer