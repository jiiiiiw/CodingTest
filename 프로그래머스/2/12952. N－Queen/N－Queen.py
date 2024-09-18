def solution(n):
    # 퀸의 위치를 저장할 배열
    result = 0
    cols = [0] * n  # cols[i]는 i행에 있는 퀸의 열 위치를 저장

    # 유효성 검사 함수: 퀸을 두었을 때 같은 열, 대각선에 있는지 검사
    def is_valid(row):
        for i in range(row):
            # 같은 열에 있거나, 대각선에 있으면 False
            if cols[i] == cols[row] or abs(cols[i] - cols[row]) == row - i:
                return False
        return True

    # 백트래킹을 통한 퀸 배치
    def place_queens(row):
        nonlocal result # 외부함수 변수 사용
        if row == n:
            result += 1
            return

        for col in range(n):
            cols[row] = col
            if is_valid(row):
                place_queens(row + 1)

    # 퀸 배치 시작
    place_queens(0)
    return result