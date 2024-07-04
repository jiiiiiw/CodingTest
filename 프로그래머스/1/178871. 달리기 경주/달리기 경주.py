def solution(players, callings):
    players_dict = dict()
    for idx, values in enumerate(players):
        players_dict[values] = idx
    
    for call in callings:
        rank = players_dict[call]
        
        players_dict[call] -=1
        players_dict[players[rank-1]] +=1
        
        players[rank-1], players[rank] = call, players[rank-1]
                
    answer = players
    return answer