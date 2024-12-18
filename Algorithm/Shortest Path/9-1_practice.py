import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)] #리스트 컴프리헨션 이거 맞나? 0도 포함함
visited = [False]*(n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    for j in range(n+1):
        if j == a:
            graph[j].append((b,c))

def shortest():
    node_length = INF
    node = 0
    for i in range(n+1):
        if distance[i] < node_length and not visited[i]:
            node_length = distance[i]
            node = i
    return node

def dijkstra(start_node):
    distance[start_node] = 0
    visited[start_node] = True
    for j in graph[start_node]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = shortest()
        visited[now] = True
        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
    for k in distance:
        if not k == INF:
            print(k)
        
def dijkstra2(start_node):
    distance[start_node] = 0
    for i in range(n):
        now = shortest()
        visited[now] = True
        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
    for k in distance:
        if not k == INF:
            print(k)
dijkstra2(start)

    

