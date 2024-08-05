from heapq import heappush, heappop

def solution(maps):
    R, C = len(maps), len(maps[0])
    
    maps = [[float("inf") if maps[r][c] else 0 for c in range(C)] for r in range(R)] # 지나온 1과 새로운 1을 구분해주기 위한 무한으로의 표현
    # print(maps)
    
    # [1,0,9,10,11]
    # [2,0,8,0,inf]
    # [3,0,7,8,9]
    # [4,5,6,0,10]
    # [0,0,0,0,11] -> flooding 알고리즘을 활용해보자
    
    maps[0][0] = 1
    QUEUE = []
    heappush(QUEUE, (1,0,0)) # 몇칸, r, c
    # print(QUEUE)
    
    while QUEUE:
        cv, cr, cc = heappop(QUEUE)
        for rd, cd in ((-1,0),(0,1),(1,0),(0,-1)):
            nr, nc = cr + rd, cc + cd
            if nr in range(R) and nc in range(C) and maps[nr][nc]:
                if cv + 1 < maps[nr][nc]:
                    maps[nr][nc] = cv + 1
                    heappush(QUEUE, (maps[nr][nc],nr,nc))
    return -1 if maps[R-1][C-1] == float("inf") else maps[R-1][C-1]
                    
    # bfs 를 큐를 통해 구현한 모습