def solution(players, callings):
    # callings에서 나오는 이름을 players에서 탐색 하지 않는다. 시간 너무 많아
    # name:rank의 딕셔너리를 만들어서 좋은 시간효율을 뽑아내버리자
    name2rank = {name:rank for rank, name in enumerate(players)}
    
    # print(name2rank)
    
    for name in callings:
        # 현재 호명된 선수의 등수 가져오기
        rank = name2rank[name]
        # 추월하는 로직을 구현
        players[rank-1], players[rank] = players[rank], players[rank-1] # 스와핑
        #r2n도 업데이트
        name2rank[players[rank]] = rank
        name2rank[players[rank-1]] = rank-1
    
    return players