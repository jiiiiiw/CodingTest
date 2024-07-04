def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for sk in skip:
        alphabet = alphabet.replace(sk, '')
    
    for a in s:
        idx = (alphabet.index(a) + index ) % len(alphabet)
        answer += alphabet[idx]
    
    return answer