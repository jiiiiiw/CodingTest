from collections import deque

def bfs(start, target, maps):
    rows = len(maps)
    cols = len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    queue = deque([start])
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    distance = [[0] * cols for _ in range(rows)]
    
    while queue:
        x, y = queue.popleft()
        
        # 목표 지점에 도달하면 이동 거리를 반환
        if (x, y) == target:
            return distance[x][y]
        
        # 상, 하, 좌, 우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 미로를 벗어나지 않고, 벽이 아니며, 방문하지 않은 칸인 경우
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    # 목표 지점에 도달할 수 없을 경우
    return -1

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # 출발점, 레버, 출구의 위치를 찾는다
    start = lever = exit = None
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':  # 시작점
                start = (i, j)
            elif maps[i][j] == 'L':  # 레버
                lever = (i, j)
            elif maps[i][j] == 'E':  # 출구
                exit = (i, j)
    
    # 1. 출발점에서 레버까지의 최단 경로를 구한다
    dist_to_lever = bfs(start, lever, maps)
    
    # 레버까지 도달할 수 없으면 -1 반환
    if dist_to_lever == -1:
        return -1
    
    # 2. 레버에서 출구까지의 최단 경로를 구한다
    dist_to_exit = bfs(lever, exit, maps)
    
    # 출구까지 도달할 수 없으면 -1 반환
    if dist_to_exit == -1:
        return -1
    
    # 3. 두 경로의 합이 탈출하는데 걸리는 최소 시간
    return dist_to_lever + dist_to_exit
