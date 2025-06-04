def solution(phone_book):
    answer = True
    phone_book.sort()
    new_book = phone_book[1:]
    for p, n in zip(phone_book, new_book):
        p_len = len(p)
        if p == n[:p_len]: return False
        
    return answer