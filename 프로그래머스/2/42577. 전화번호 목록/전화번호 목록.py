# 사전순으로 정렬해주는 sort의 특징을 이용하자

def solution(phone_book):
    phone_book = sorted(phone_book)
    for f_idx in range(len(phone_book)-1):
        b_idx = f_idx + 1
        f_num = phone_book[f_idx]
        b_num = phone_book[b_idx]
        if f_num == b_num[:len(f_num)]:
            return False
    return True