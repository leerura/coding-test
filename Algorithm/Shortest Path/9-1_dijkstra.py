import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 개수, 간선 개수
n,m = map(int, input().split())
#시작 노드 번호
start = int(input())
#그래프 정보
graph = [[] for i in range(n+1)] #노드 0부터 시작
#방문정보
visited = [False] * (n+1)
#최단 거리 테이블
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1): #0번 노드는 빈칸
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return(index)

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] #거리 업데이트
    #젤 작은 거 찾고 업데이트 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])