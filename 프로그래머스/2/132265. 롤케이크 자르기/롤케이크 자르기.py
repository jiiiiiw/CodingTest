def solution(topping):
    right_num, left_num = [], []
    right_set, left_set = set(), set()

    for top in topping:
        right_set.add(top)
        right_num.append(len(right_set))

    for top in topping[::-1]:
        left_set.add(top)
        left_num.append(len(left_set))

    len_left = len(left_num)
    answer = [i for i in range(len(right_num) - 1) if right_num[i] == left_num[len_left - i - 2]]

    return len(answer)