def solution(data, col, row_begin, row_end):
    # 1. 주어진 col 번째 컬럼을 기준으로 오름차순 정렬, 
    # 값이 같다면 첫 번째 컬럼을 기준으로 내림차순 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    result = 0
    
    # 2. row_begin부터 row_end까지 S_i 값을 XOR로 누적
    for i in range(row_begin - 1, row_end):
        S_i = sum([value % (i + 1) for value in data[i]])
        result ^= S_i
    
    return result
