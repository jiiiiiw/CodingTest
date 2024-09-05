def solution(maps):
    # 지도 크기
    rows = len(maps)
    cols = len(maps[0])
    
    # 방문 여부를 저장하는 배열
    visited = [[False] * cols for _ in range(rows)]
    
    # 상하좌우 이동을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        stack = [(x, y)]
        total_food = 0
        
        while stack:
            cx, cy = stack.pop()
            
            # 이미 방문한 곳은 무시
            if visited[cx][cy]:
                continue
                
            visited[cx][cy] = True
            total_food += int(maps[cx][cy])  # 현재 위치의 식량을 더함
            
            # 상하좌우 탐색
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                
                # 지도를 벗어나지 않고, 방문하지 않았으며, 바다가 아닌 경우
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    stack.append((nx, ny))
        
        return total_food
    
    # 모든 무인도에서 머무를 수 있는 날수를 저장할 리스트
    islands = []
    
    # 지도 탐색
    for i in range(rows):
        for j in range(cols):
            # 숫자가 적힌 섬이면서 방문하지 않은 경우
            if maps[i][j] != 'X' and not visited[i][j]:
                islands.append(dfs(i, j))
    
    # 섬이 없으면 -1 반환
    if not islands:
        return [-1]
    
    # 오름차순 정렬하여 반환
    return sorted(islands)
