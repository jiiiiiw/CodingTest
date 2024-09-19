def solution(cards):
    n = len(cards)
    visited = [False] * n  # 각 상자가 방문되었는지 여부를 기록하는 배열
    cycles = []  # 각 사이클의 크기를 저장할 리스트

    # 사이클을 찾는 함수
    def find_cycle(start):
        count = 0
        current = start
        
        while not visited[current]:
            visited[current] = True  # 현재 상자를 방문 표시
            current = cards[current] - 1  # 다음 상자를 가리킴 (0-index로 변환)
            count += 1
        
        return count

    # 모든 상자에 대해 사이클 찾기
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 상자에서 사이클을 찾음
            cycle_size = find_cycle(i)
            cycles.append(cycle_size)

    # 사이클 크기가 2개 미만이면 0점
    if len(cycles) < 2:
        return 0

    # 사이클 크기 내림차순 정렬 후 두 개의 가장 큰 값 곱하기
    cycles.sort(reverse=True)
    return cycles[0] * cycles[1]