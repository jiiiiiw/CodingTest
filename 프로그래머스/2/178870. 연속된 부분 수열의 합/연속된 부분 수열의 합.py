# 투 포인터를 활용해보자
# 합이 작으면 오른쪽 포인터 이동, 크거나 같으면 다음 왼쪽 포인터를 이동시킨다.

def solution(sequence, k):
    answer = []
    right = 0
    count = 0
    
    for left in range(len(sequence)):
        
        while right < len(sequence) and count < k:
            count += sequence[right]
            right += 1
        
        if count == k:
            if not answer:
                answer = [left, right-1]
            else: # 저장된 길이가 짧은지 확인
                answer = [left, right-1] if answer[1] - answer[0] > right - 1 - left else answer
        
        count -= sequence[left]    
    
    return answer