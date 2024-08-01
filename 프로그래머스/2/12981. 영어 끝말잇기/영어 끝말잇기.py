def solution(n, words):
    # 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
    # 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
    # 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
    # 이전에 등장했던 단어는 사용할 수 없습니다.
    # 한 글자인 단어는 인정되지 않습니다.
    
    used = set() # set은 해쉬화되어 있어서 검색 시, 상수시간만이 걸린다.\
    for idx in range(len(words)):
        userNum = (idx % n) + 1
        Turn = (idx // n) + 1
        if 1 < len(words[idx]) and words[idx] not in used:
            if idx == 0:
                used.add(words[idx])
            elif words[idx-1][-1] == words[idx][0]:
                used.add(words[idx])
            else:
                return [userNum, Turn]
        else:
            return [userNum, Turn]
    return [0,0]