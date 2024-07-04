def solution(park, routes):
    
    move_dic = {'E':[0,1],'W':[0,-1],'S':[1,0],'N':[-1,0]}
    H,W = len(park)-1,len(park[0])-1

    robot = [0,0]
    for i,x in enumerate(park):
        if 'S' not in x: continue   
        for j,y in enumerate(x):
            if 'S'==y:
                robot=[i,j]        
                park[i]= park[i].replace('S','O')  
                break
                
    for route in routes:
        cur = robot                
        direction, walks = route.split(" ")
        for _ in range(int(walks)):
            x,y = cur[0]+move_dic[direction][0],cur[1]+move_dic[direction][1]
            if (x>H or x<0 or y>W or y<0) or ('X' == park[x][y]):
                cur = robot
                break
            else:
                cur=[x,y]
        robot=cur
        
    return robot