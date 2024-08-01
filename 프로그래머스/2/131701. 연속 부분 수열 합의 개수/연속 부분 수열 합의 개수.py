def solution(elements):
    offset = 1
    curr_sums = elements[:]
    partial_sums = set(curr_sums)
    while offset < len(elements):
        for i in range(len(elements)):
            curr_sums[i] += elements[(i+offset)%len(elements)]
            partial_sums.add(curr_sums[i])
        offset += 1
    return len(partial_sums)