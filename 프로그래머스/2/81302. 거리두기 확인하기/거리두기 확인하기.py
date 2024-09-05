# 각 대기실의 거리두기를 지키는지 검사하는 함수
def check_place(place):
    # 5x5 대기실을 탐색
    for i in range(5):
        for j in range(5):
            # 응시자가 앉아있는 경우(P)
            if place[i][j] == 'P':
                # 상, 하, 좌, 우에 대한 검사 (맨해튼 거리 1)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        return 0  # 거리두기 실패
                
                # 맨해튼 거리 2인 경우 검사
                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        # 사이에 파티션이 없으면 거리두기 실패
                        if place[i + dx // 2][j + dy // 2] != 'X':
                            return 0

                # 대각선에 대한 검사 (맨해튼 거리 2)
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        # 두 칸 중 하나라도 파티션이 없으면 거리두기 실패
                        if not (place[i][nj] == 'X' and place[ni][j] == 'X'):
                            return 0
    return 1  # 거리두기 성공

# 모든 대기실에 대해 거리두기를 검사하는 함수
def solution(places):
    answer = []
    for place in places:
        answer.append(check_place(place))
    return answer
