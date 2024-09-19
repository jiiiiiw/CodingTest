def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        
        max_block = 1  # i의 약수 중 가장 큰 블록 번호
        
        # i의 약수 탐색 (1부터 sqrt(i)까지)
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:  # j가 약수일 때
                other = i // j  # j에 대응하는 약수
                
                # 10,000,000 이하의 약수 중 큰 값을 찾음
                if other <= 10**7:
                    max_block = max(max_block, other)
                if j <= 10**7:
                    max_block = max(max_block, j)
        
        answer.append(max_block)
    
    return answer