def solution(grid):
    global n,m
    answer = []
    n,m = len(grid),len(grid[0])
    lists = [[[0,0,0,0]for i in range(m)] for i in range(n)] # 3차원 리스트를 구현하기
    
    for i in range(n):
        grid[i] = list(grid[i])
    
    for c in range(n):
        for r in range(m):
            for k in range(4):
                if lists[c][r][k] != 0:   continue
                cnt = cycle(lists,grid,c,r,k)-1
                answer.append(cnt)
                
    answer.sort()
    return answer


def cycle(coord,grid, i, j, out):
    cnt = 1
    while coord[i][j][out] != 1:
        coord[i][j][out] = cnt
        cnt += 1
        if grid[i][j] == "S": pass
        elif grid[i][j] == "L":
            if out == 0:   out = 2
            elif out == 1:   out = 3
            elif out == 2:   out = 1
            else:   out = 0
        else:
            if out == 0:   out = 3
            elif out == 1:   out = 2
            elif out == 2:   out = 0
            else:   out = 1
            
        i,j = route(out,i,j)
    return cnt


def route(out, i,j):
    if out == 0:   
        i -= 1
        if i < 0:   i = n-1
    elif out == 1:   
        i += 1
        if i >n -1 :    i = 0
    elif out == 2:   
        j -= 1
        if j < 0:   j = m-1
    else: 
        j += 1
        if j > m -1 :    j = 0
    return  i, j