def solution(board):
    # 1. O와 X의 개수 세기
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)
    
    # 2. 승리 조건을 확인하는 함수 (가로, 세로, 대각선)
    def is_winner(player):
        # 가로와 세로 체크
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):  # 가로
                return True
            if all(board[j][i] == player for j in range(3)):  # 세로
                return True
        # 대각선 체크
        if all(board[i][i] == player for i in range(3)):  # 왼쪽 대각선
            return True
        if all(board[i][2-i] == player for i in range(3)):  # 오른쪽 대각선
            return True
        return False

    o_wins = is_winner('O')
    x_wins = is_winner('X')

    # 3. 규칙 위반 여부 확인
    # (1) X가 O보다 많이 두어진 경우
    if x_count > o_count:
        return 0
    # (2) O가 X보다 두 개 이상 많이 두어진 경우
    if o_count > x_count + 1:
        return 0
    # (3) O가 승리했는데 X가 추가로 두어진 경우
    if o_wins and o_count != x_count + 1:
        return 0
    # (4) X가 승리했는데 O가 더 많이 두어진 경우
    if x_wins and o_count != x_count:
        return 0
    # (5) O와 X가 동시에 승리한 경우
    if o_wins and x_wins:
        return 0

    # 규칙 위반이 없으면 1 반환
    return 1
