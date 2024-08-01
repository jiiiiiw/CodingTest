def solution(people, limit):
    answer = 0
    people.sort()
    lidx, hidx = 0, len(people) - 1
    while lidx < hidx:
        if people[lidx] + people[hidx] <= limit:
            lidx += 1
            hidx -= 1
        else:
            hidx -= 1
        answer += 1
    if hidx == lidx:
        answer += 1
    
    return answer