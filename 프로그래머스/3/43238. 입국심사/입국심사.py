def solution(n, times):
    l = 1
    r = max(times) * n
    answer = r

    while l <= r:
        mid = (l + r) // 2

        total = sum(mid // time for time in times)

        if total >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer