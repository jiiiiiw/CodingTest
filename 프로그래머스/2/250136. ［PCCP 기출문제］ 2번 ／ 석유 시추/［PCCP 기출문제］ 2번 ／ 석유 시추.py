def solution(land):
    n = len(land)
    m = len(land[0]) if n > 0 else 0

    visited = [[False] * m for _ in range(n)]
    chunk_map = [[-1] * m for _ in range(n)]
    
    def dfs(x, y, chunk_id):
        stack = [(x, y)]
        size = 0
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            chunk_map[cx][cy] = chunk_id
            size += 1
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    stack.append((nx, ny))
        
        return size

    # Find oil chunks
    chunk_sizes = {}
    chunk_id = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size = dfs(i, j, chunk_id)
                chunk_sizes[chunk_id] = size
                chunk_id += 1

    # Map chunk sizes to columns, ensuring no duplicates within a column
    max_oil = 0
    for j in range(m):
        seen_chunks = set()  # To ensure no duplicates within a column
        oil_sum = 0
        for i in range(n):
            chunk_id = chunk_map[i][j]
            if chunk_id != -1 and chunk_id not in seen_chunks:
                oil_sum += chunk_sizes[chunk_id]
                seen_chunks.add(chunk_id)
        max_oil = max(max_oil, oil_sum)

    return max_oil