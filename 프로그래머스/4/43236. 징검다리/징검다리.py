def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left = 1
    right = distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        last = 0
        change = 0

        for rock in rocks:
            gap = rock - last
            if gap < mid:
                change += 1
            else:
                last = rock

        if change > n:
            right = mid - 1
        else: 
            answer = mid
            left = mid + 1

    return answer