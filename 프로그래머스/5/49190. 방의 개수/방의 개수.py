def solution(a):
    d = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    v = set() 
    e = set()  
    x, y = 0, 0
    v.add((x,y))
    cnt = 0
    
    for i in a:
        for _ in range(2):  
            nx, ny = x + d[i][0] * 0.5, y + d[i][1] * 0.5
            if ((x,y), (nx,ny)) not in e:
                if (nx,ny) in v:
                    cnt += 1
                v.add((nx,ny))
                e.add(((x,y), (nx,ny)))
                e.add(((nx,ny), (x,y)))
            x, y = nx, ny
    return cnt