from collections import deque

def solution(board):
    # 보드 크기
    n, m = len(board), len(board[0])
    
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 로봇의 시작점과 목표 지점 찾기
    start, goal = None, None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
    
    # BFS를 위한 큐와 방문 기록
    queue = deque([(start[0], start[1], 0)])  # (x좌표, y좌표, 이동 횟수)
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    # BFS 탐색 시작
    while queue:
        x, y, cnt = queue.popleft()
        
        # 목표 지점에 도달하면 이동 횟수 반환
        if (x, y) == goal:
            return cnt
        
        # 4방향으로 이동
        for dx, dy in directions:
            nx, ny = x, y
            
            # 벽이나 장애물에 부딪힐 때까지 이동
            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            
            # 이동한 위치가 방문하지 않은 위치라면 큐에 추가
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
    
    # 목표 지점에 도달할 수 없다면 -1 반환
    return -1
