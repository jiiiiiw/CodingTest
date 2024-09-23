def solution(name):
    # 알파벳 변경에 필요한 조작 횟수를 계산하는 함수
    def alphabet_to_moves(char):
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    n = len(name)
    
    # 각 문자를 변경하는 데 필요한 상하 조작 횟수의 합
    change_count = sum(alphabet_to_moves(char) for char in name)
    
    # 모든 문자가 'A'인 경우 조작이 필요 없음
    if change_count == 0:
        return 0
    
    # 최소 좌우 이동 횟수 (최악의 경우: 모든 문자를 순서대로 변경)
    min_move = n - 1
    
    for i in range(n):
        # 현재 위치에서 오른쪽으로 이동하며 처음 만나는 'A'가 아닌 문자의 위치
        next_non_a = i + 1
        while next_non_a < n and name[next_non_a] == 'A':
            next_non_a += 1
        
        # 현재까지의 이동거리 + 뒤로 돌아가는 거리 + 남은 문자들까지의 거리
        distance = i + i + (n - next_non_a)
        
        # 앞으로 가는 것과 뒤로 가는 것 중 최소값 선택
        distance = min(distance, i + 2 * (n - next_non_a))
        
        # 최소 이동 횟수 업데이트
        min_move = min(min_move, distance)
    
    return change_count + min_move