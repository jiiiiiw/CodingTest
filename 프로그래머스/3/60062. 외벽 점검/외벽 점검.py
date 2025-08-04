from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    extended_weak = weak + [w + n for w in weak]
    min_friends = len(dist) + 1

    for start in range(length):
        for friends in permutations(dist):
            count = 1
            coverage = extended_weak[start] + friends[0]

            for idx in range(start, start + length):
                if extended_weak[idx] > coverage:
                    count += 1
                    if count > len(dist):
                        break
                    coverage = extended_weak[idx] + friends[count - 1]

            min_friends = min(min_friends, count)

    return min_friends if min_friends <= len(dist) else -1