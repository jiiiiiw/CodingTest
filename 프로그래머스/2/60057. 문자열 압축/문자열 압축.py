def solution(s):
    # 입력 문자열 s의 길이
    n = len(s)
    
    # 가장 짧은 압축 길이를 큰 값으로 초기화
    min_length = n
    
    # 1부터 n//2까지의 단위로 문자열을 자름
    for size in range(1, n // 2 + 1):
        compressed = ""
        prev = s[:size]  # 첫 번째 덩어리
        count = 1  # 덩어리 반복 횟수
        
        # size 크기 단위로 문자열을 잘라가며 비교
        for i in range(size, n, size):
            # 다음 덩어리와 이전 덩어리를 비교
            if prev == s[i:i+size]:
                count += 1  # 반복되면 카운트 증가
            else:
                # 이전 덩어리가 반복되었으면 압축
                compressed += (str(count) + prev) if count > 1 else prev
                # 새로운 덩어리로 초기화
                prev = s[i:i+size]
                count = 1
        
        # 남은 마지막 덩어리 처리
        compressed += (str(count) + prev) if count > 1 else prev
        
        # 압축된 문자열의 길이로 최소 길이 갱신
        min_length = min(min_length, len(compressed))
    
    return min_length
