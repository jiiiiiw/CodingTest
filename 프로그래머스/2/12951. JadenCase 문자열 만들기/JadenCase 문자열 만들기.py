def solution(s):
    answer = ""
    vaild = True
    for char in s:
        if vaild:
            if char == " ":
                answer += char
                vaild = True
            elif char.isdigit():
                answer += char
                vaild = False
            elif char.isalpha():
                answer += char.upper()
                vaild = False
        else:
            if char == " ":
                vaild = True
            answer += char.lower()
    return answer
                