import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1) 

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

q = []
def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(distance[i[0]], i[0]) )

dijkstra(start)

for i in distance:
    if i != INF:
        print(i)
