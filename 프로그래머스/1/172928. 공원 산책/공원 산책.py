def solution(park, routes):
    # 문자열로 표시된 지도를 인덱스로의 전처리 과정을 거칠 것! like 이중배열
    # 1이 장애물 0이 가능한 길
    ROW, COL = len(park), len(park[0]) # 각각의 맥시멈 뽑기
    gird = [[0 for c_idx in range(COL)] for r_idx in range(ROW)] # 외부 내부 헷갈리지 말자
    curr_row, curr_col = 0, 0 # 시작 위치를 정의
    for r_idx in range(ROW):
        for c_idx in range(COL):
            if park[r_idx][c_idx] == "X":
                gird[r_idx][c_idx] = 1
            elif park[r_idx][c_idx] == "S":
                curr_row, curr_col = r_idx, c_idx
    
    dirs = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)} # 방향을 벡터값으로 기록
    
    for route in routes:
        direction, distance = route.split()
        dir_row, dir_col = dirs[direction]
        
        vaild = True
        for offset in range(1, int(distance)+1):
            new_row, new_col = curr_row + dir_row * offset, curr_col + dir_col * offset
            if new_row in range(ROW) and new_col in range(COL) and gird[new_row][new_col] == 0:
                pass
            else:
                vaild = False
            
        if vaild:
            curr_row, curr_col = new_row, new_col
            
    return [curr_row, curr_col]