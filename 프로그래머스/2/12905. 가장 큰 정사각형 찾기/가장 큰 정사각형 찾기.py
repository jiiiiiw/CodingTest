def solution(board):
    # 행(row)와 열(column)의 크기
    n = len(board)
    m = len(board[0])
    
    # dp 테이블 초기화 (입력 배열과 동일한 크기)
    dp = [[0] * m for _ in range(n)]
    max_side = 0  # 가장 큰 정사각형의 변의 길이
    
    # 첫 번째 행과 첫 번째 열은 그대로 사용
    for i in range(n):
        dp[i][0] = board[i][0]
        max_side = max(max_side, dp[i][0])
        
    for j in range(m):
        dp[0][j] = board[0][j]
        max_side = max(max_side, dp[0][j])
    
    # 나머지 셀에 대해 DP 계산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    # 가장 큰 정사각형의 넓이를 반환 (변의 길이의 제곱)
    return max_side * max_side
