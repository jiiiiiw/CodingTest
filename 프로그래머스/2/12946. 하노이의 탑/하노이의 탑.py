def solution(n):
    # 결과를 저장할 리스트
    moves = []
    
    # 재귀적으로 하노이 탑을 해결하는 함수
    def hanoi(n, from_pole, to_pole, aux_pole):
        if n == 1:
            # 원판 1개를 옮기는 경우
            moves.append((from_pole, to_pole))
        else:
            # n-1개 원판을 aux_pole로 옮김
            hanoi(n-1, from_pole, aux_pole, to_pole)
            # 가장 큰 원판을 to_pole로 옮김
            moves.append((from_pole, to_pole))
            # aux_pole에 있는 n-1개 원판을 to_pole로 옮김
            hanoi(n-1, aux_pole, to_pole, from_pole)
    
    # 하노이 탑 문제를 시작합니다.
    hanoi(n, 1, 3, 2)
    
    return moves
