def time_convert(string) :
    h, m = map(int, string.split(":"))
    return h*60 + m

def solution(book_time):
    answer = 0
    time = list()
    for start, end in book_time :
        time.append((time_convert(start), 1))
        time.append((time_convert(end)+10, 0))
    
    time.sort()
    
    tmp = 0
    for t, c in time :
        tmp += -1 if c == 0 else 1
        answer = max(answer, tmp)
    return answer