# n = 1: 1 ...................................... -> 1
# n = 2: 11, 2 ................................. -> 2
# n = 3: 111, 21, 12 ........................  -> 3
# n = 4: 1111, 211, 112, 121, 22  ....... -> 5

# a[3] = 3 = a[1] + a[2]
# a[4] = 5 = a[2] + a[3]
# .
# .
# a[n] = a[n-1] + a[n-2]

def solution(n):
    tile = [0 for i in range(n)]
    tile[0], tile[1] = 1, 2
    for i in range(2, n):
        tile[i] = (tile[i-1] + tile[i-2]) % 1000000007

    return tile[n-1]