def solution(dirs):
    
    moves = {
        'U' : [1, 0],
        'D' : [-1, 0],
        'R' : [0, 1],
        'L' : [0, -1]
    }
    
    visited = set()
    crryx = [0, 0]
    
    for dir in dirs:
        dy, dx = moves[dir]
        newy = crryx[0] + dy
        newx = crryx[1] + dx
        
        if -5<=newy<=5 and -5<=newx<=5:
            visited.add(((crryx[0],crryx[1]),(newy,newx)))
            visited.add(((newy,newx),(crryx[0],crryx[1])))
            crryx[0] = newy
            crryx[1] = newx
    
    return len(visited) / 2