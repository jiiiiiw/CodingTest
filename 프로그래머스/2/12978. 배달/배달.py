# 연결된 노드와 거리를 담을 연결딕셔너리 dist를 만들어 준다.
# 각 노드들의 방문유무와 시간을 기록할 방문리스트 visited 생성
# 1번 노드부터 deq에 넣고 노드와 인접한 노드들중 시간이 K보다 작거나 같고, 한번도 방문하지 않았거나 방문했더라도 현재 걸린 시간이 기록된 시간보다 짧으면 visited를 갱신해주고 deq에 노드를 넣어준다.
# while문이 끝나면 visited에서 0을 제외한 숫자들의 개수를 구함 (0은 제한 시간 내에 방문하지 못한 노드이기 때문)

INF = 10000*50

def solution(N, road, K):
    answer = 0
    
    visited = [-1]*(N+1)
    time = [INF]*(N+1)
    
    visited[0] = 0
    time[1] = 0
    
    graph = [[INF]*(N+1) for i in range(N+1)]
    
    for check in road:
        if graph[check[0]][check[1]] > check[2]:
            graph[check[0]][check[1]] = check[2]
            graph[check[1]][check[0]] = check[2]
    
    
    dijkstra(visited, time, graph)
    
    for i in time:
        if i <= K:
            answer += 1
    
    return answer


def dijkstra(visited, time, graph):
    
    index = findMin(visited, time)
    
    if index == 0:
        return 0
    
    visited[index] = 0
    for i in range(len(graph[index])):
        if graph[index][i] != INF:
            if time[i] > time[index] + graph[index][i]:
                time[i] = time[index] + graph[index][i]
    
    return dijkstra(visited, time, graph)


def findMin(visited, time):
    value = INF
    index = 0
    for i in range(len(time)):
        if visited[i] == -1 and time[i] < value:
            value = time[i]
            index = i
    return index