def solution(s):
    Stack = []
    for bracket in s:
        if bracket == "(":
            Stack.append(bracket)
        elif bracket == ")":
            if Stack and Stack[-1] == "(":
                Stack.pop()
            else:
                Stack.append(bracket)
    # print(Stack)
    return False if Stack else True